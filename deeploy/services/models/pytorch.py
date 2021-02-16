from typing import Any
from os.path import join

from torch.nn import Module
from torch import save

from . import BaseModel


class PyTorchModel(BaseModel):

    __pytorch_model: Module

    def __init__(self, model_object: Any) -> None:

        if not issubclass(type(model_object), Module):
            raise Exception('Not a valid PyTorch class')

        self.__pytorch_model = model_object
        return

    def save(self, local_folder_path: str) -> None:
        save(self.__pytorch_model.state_dict(),
             join(local_folder_path, 'model.pt'))
        return
