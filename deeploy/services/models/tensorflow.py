from typing import Any

from tensorflow.keras import Model

from . import BaseModel


class TensorFlowModel(BaseModel):

    __tensorflow_model: Model

    def __init__(self, model_object: Any) -> None:

        if not issubclass(type(model_object), Model):
            raise Exception('Not a valid TensorFlow class')

        self.__tensorflow_model = model_object
        return

    def save(self, local_folder_path: str) -> None:
        self.__tensorflow_model.save(local_folder_path)
        return
