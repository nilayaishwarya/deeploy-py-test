from pydantic import BaseModel
from typing import List, Dict, Any
from deeploy.models import PredictionLog


class PredictionLogs(BaseModel):
    data: List[PredictionLog]
    count: int
