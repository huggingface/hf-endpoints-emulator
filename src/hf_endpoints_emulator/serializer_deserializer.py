import json
from io import BytesIO

from PIL import Image


def decode_bytes(body):
    return {"inputs": bytes(body)}


def decode_json(body):
    return json.loads(body)


def decode_image(body):
    image = Image.open(BytesIO(body)).convert("RGB")
    return {"inputs": image}


def encode_json(body):
    return json.dumps(body)


content_type_mapping = {
    "application/json": decode_json,
    "text/csv": None,
    "text/plain": None,
    # image types
    "image/png": decode_image,
    "image/jpeg": decode_image,
    "image/jpg": decode_image,
    "image/tiff": decode_image,
    "image/bmp": decode_image,
    "image/gif": decode_image,
    "image/webp": decode_image,
    "image/x-image": decode_image,
    # audio types
    "audio/x-flac": decode_bytes,
    "audio/flac": decode_bytes,
    "audio/mpeg": decode_bytes,
    "audio/wave": decode_bytes,
    "audio/wav": decode_bytes,
    "audio/x-wav": decode_bytes,
    "audio/ogg": decode_bytes,
    "audio/x-audio": decode_bytes,
    "audio/webm": decode_bytes,
    "audio/webm;codecs=opus": decode_bytes,
}


def decode(body, content_type):
    return content_type_mapping[content_type](body)


def encode(body, accept):
    return encode_json(body)
