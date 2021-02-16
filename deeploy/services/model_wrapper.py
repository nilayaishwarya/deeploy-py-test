from typing import Any, List
import inspect

from deeploy.enums import ModelType
from deeploy.services.ml_models import BaseModel


class ModelWrapper:

    __model_helper: BaseModel

    def __init__(self, model_object: Any) -> None:

        self.__model_helper = self.__get_model_helper(model_object)

        return

    def save(self, local_folder_path: str) -> None:
        self.__model_helper.save(local_folder_path)
        return

    def __get_model_type(self, model_object: Any) -> ModelType:

        base_classes = list(map(lambda x: x.__module__ + '.' +
                                x.__name__, inspect.getmro(type(model_object))))

        if self.__is_sklearn(base_classes):
            return ModelType.SKLEARN
        if self.__is_xgboost(base_classes):
            return ModelType.XGBOOST
        if self.__is_pytorch(base_classes):
            return ModelType.PYTORCH
        if self.__is_tensorflow(base_classes):
            return ModelType.TENSORFLOW
        if self.__is_triton(base_classes):
            return ModelType.TRITON
        if self.__is_onnx(base_classes):
            return ModelType.ONNX

        raise NotImplementedError(
            'This model type is not implemented by Deeploy')

    def __get_model_helper(self, model_object) -> BaseModel:

        model_type = self.__get_model_type(model_object)

        # only import the helper class when it is needed
        if model_type == ModelType.SKLEARN:
            from deeploy.services.models import SKLearnModel
            return SKLearnModel(model_object)
        if model_type == ModelType.XGBOOST:
            from deeploy.services.models import XGBoostModel
            return XGBoostModel(model_object)
        if model_type == ModelType.PYTORCH:
            from deeploy.services.models import PyTorchModel
            return PyTorchModel(model_object)
        if model_type == ModelType.TENSORFLOW:
            from deeploy.services.models import TensorFlowModel
            return TensorFlowModel(model_object)
        if model_type == ModelType.TRITON:
            from deeploy.services.models import TritonModel
            return TritonModel(model_object)
        if model_type == ModelType.ONNX:
            from deeploy.services.models import ONNXModel
            return ONNXModel(model_object)

    def __is_sklearn(self, base_classes: List[str]) -> bool:
        return 'sklearn.base.BaseEstimator' in base_classes and not 'xgboost.sklearn.XGBModel' in base_classes

    def __is_xgboost(self, base_classes: List[str]) -> bool:
        return 'xgboost.sklearn.XGBModel' in base_classes

    def __is_pytorch(self, base_classes: List[str]) -> bool:
        return 'torch.nn.modules.module.Module' in base_classes

    def __is_tensorflow(self, base_classes: List[str]) -> bool:
        return 'tensorflow.keras.Model' in base_classes

    def __is_onnx(self, model: Any) -> bool:
        # TODO
        return False

    def __is_triton(self, model: Any) -> bool:
        # TODO
        return False
