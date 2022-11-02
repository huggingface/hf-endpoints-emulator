import os
from typing import Dict, List, Any


class EndpointHandler:
    def __init__(self, path=""):
        # Preload all the elements you are going to need at inference.
        # pseudo:
        # self.model= load_model(path)
        os.listdir(path)

    def __call__(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
         data args:
              inputs (:obj: `str` | `PIL.Image` | `np.array`)
              kwargs
        Return:
              A :obj:`list` | `dict`: will be serialized and returned
        """
        inputs = data.pop("inputs", data)

        # reverese the string
        result = inputs[::-1]
        return {"outputs": result}
