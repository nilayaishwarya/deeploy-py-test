from typing import Any
from os.path import join

from xgboost import XGBClassifier
from joblib import dump

from . import BaseModel


class XGBoostModel(BaseModel):

    __xgboost_model: XGBClassifier

    def __init__(self, model_object: Any) -> None:

        if not issubclass(type(model_object), XGBClassifier):
            raise Exception('Not a valid XGBoost class')

        self.__xgboost_model = model_object
        return

    def save(self, local_folder_path: str) -> None:
        self.__xgboost_model.save_model(join(local_folder_path, 'model.bst'))
        return
