from onnx import ModelProto

from . import BaseModel


class ONNXModel(BaseModel):
    # TODO
    def save(self, local_folder_path: str) -> None:
        return