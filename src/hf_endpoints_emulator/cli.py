import typer

from .emulator import emulate as pkg_emulate


app = typer.Typer()


@app.command()
def emulate(handler: str = "handler.py", port: int = 5000):
    """
    Provider you Inference Endpoints Handler and the port to run the server on.

    --handler is the path to your handler.py file, default is handler.py
    --port is the port to run the server on, default: 5000
    """
    pkg_emulate(handler=handler, port=port)


if __name__ == "__main__":
    app()
