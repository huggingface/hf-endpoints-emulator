# Emulator for Custom Handlers for Inference Endpoints

🤗 Inference Endpoints offers a secure production solution to easily deploy any 🤗 Transformers and Sentence-Transformers models from the Hub on dedicated and autoscaling infrastructure managed by Hugging Face.

🤗 Inference Endpoints support all of the 🤗 Transformers and Sentence-Transformers tasks as well as custom tasks not supported by 🤗 Transformers yet like speaker diarization and diffusion.

The `hf_endpoints_emulator` package provides a simple way to test your custom handlers locally before deploying them to Inference Endpoints. It is also useful for debugging your custom handlers. 

The package provides a `hf_endpoints_emulator` command line tool that can be used to run your custom handlers locally. It also provides a `hf_endpoint_emulator` Python package that can be used to run your custom handlers locally from Python.

## Installation

```bash
pip install hf_endpoints_emulator
```

## Usage

You can check the `examples/` directory for examples on how to use the `hf_endpoints_emulator` package.

### Command Line

```bash
hf-endpoints-emulator --handler <handler> 
```

This will start a web server that will run your custom handler. The web server will be accessible at `http://localhost:5000`. You can then send requests to the web server to test your custom handler.

**curl**

```bash
curl --request POST \
  --url http://localhost/:5000 \
  --header 'Content-Type: application/json' \
  --data '{
        "inputs": "I like you."
}'
```

**python**

```python
import requests

url = "http://localhost:5000/"

payload = {"inputs": "test"}
headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.json())
```

## Python pacakge

```python
from hf_endpoints_emulator.emulator import emulate

emulate(handler_path="examples/my_handler.py", port=5000)
```