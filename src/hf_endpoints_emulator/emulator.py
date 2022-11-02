import importlib.util
import json
import logging
import os
import sys
from pathlib import Path

from starlette.applications import Starlette
from starlette.responses import JSONResponse, PlainTextResponse
from starlette.routing import Route

import typer
import uvicorn

from .serializer_deserializer import decode


logging.basicConfig(format="%(levelname)s:     %(message)s", datefmt="", level=logging.INFO)
logger = logging.getLogger("uvicorn.access")


async def some_startup_task():
    global inference_handler

    _handler_path = Path(os.environ.get("HANDLER_PATH", "handler.py"))
    module_name = f"{_handler_path.stem}.EndpointHandler"

    spec = importlib.util.spec_from_file_location(module_name, _handler_path)
    # add the whole directory to path for submodlues
    sys.path.insert(0, _handler_path.parents[0])
    # import custom handler
    handler = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = handler
    spec.loader.exec_module(handler)
    # init custom handler with model_dir
    inference_handler = handler.EndpointHandler(_handler_path.parents[0])
    # logger.info(f"Loaded EndpointHandler from {str(_handler_path)} file")


async def predict(request):
    try:
        content_type = request.headers.get("content-Type", None)
        deserialized_body = decode(await request.body(), content_type)
        # checks if input schema is correct
        if "inputs" not in deserialized_body:
            raise ValueError(f"Body needs to provide a inputs key, recieved: {json.dumps(deserialized_body)}")

        # run handler call
        pred = inference_handler(deserialized_body)
        return JSONResponse(pred)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=400)


async def health(request):
    return PlainTextResponse("Ok")


app = app = Starlette(
    debug=True,
    routes=[
        Route("/", health, methods=["GET"]),
        Route("/health", health, methods=["GET"]),
        Route("/", predict, methods=["POST"]),
        Route("/predict", predict, methods=["POST"]),
    ],
    on_startup=[some_startup_task],
)


def emulate(handler: str = "handler.py", port: int = 5000):
    os.environ["HANDLER_PATH"] = handler
    logger.info(f"Loading handler from {handler} file")
    uvicorn.run(app, port=port, host="0.0.0.0", log_level="info")


if __name__ == "__main__":
    typer.run(emulate)
