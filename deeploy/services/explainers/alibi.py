from typing import Any
from os.path import join

import dill
from alibi.api.interfaces import Explainer

from . import BaseExplainer


class AlibiExplainer(BaseExplainer):

    __alibi_explainer: Explainer

    def __init__(self, explainer_object: Any) -> None:

        if not issubclass(type(explainer_object), Explainer):
            raise Exception('Not a valid Alibi class')

        self.__alibi_explainer = explainer_object
        return

    def save(self, local_folder_path: str) -> None:
        with open(join(local_folder_path, 'explainer.dill'), 'wb') as f:
            dill.dump(self.__alibi_explainer, f)
        return
