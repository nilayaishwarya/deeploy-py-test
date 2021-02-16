from typing import Any
from os.path import join

from sklearn.base import BaseEstimator
from joblib import dump

from . import BaseModel


class SKLearnModel(BaseModel):

    __sklearn_model: BaseEstimator

    def __init__(self, model_object: Any) -> None:

        if not issubclass(type(model_object), BaseEstimator):
            raise Exception('Not a valid SKLearn class')

        self.__sklearn_model = model_object
        return

    def save(self, local_folder_path: str) -> None:
        dump(self.__sklearn_model, join(local_folder_path, 'model.joblib'))
        return
