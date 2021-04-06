from typing import Optional, List, Any

from pydantic import BaseModel

from deeploy.common import to_lower_camel
from deeploy.enums import ModelType, ExplainerType


class Deployment(BaseModel):
    commit_id: str
    name: str
    workspace_id: str
    description: Optional[str]
    example_input: Optional[List[Any]]
    example_output: Optional[List[Any]]
    model_type: ModelType
    model_serverless: bool
    explainer_type: Optional[ExplainerType]
    explainer_serverless: Optional[bool]
    status: int
    is_archived: bool
    s3_link: str
    owner_id: str
    repository_id: str
    kf_serving_id: Optional[str]
    public_url: Optional[str]
    id: str
    created_at: str
    updated_at: str

    class Config:
        alias_generator = to_lower_camel


class DeployOptions(BaseModel):
    """
    Class that contains the options for deploying a model

    Attributes:
      name: name of the deployment
      model_serverless: boolean indicating whether to deploy the model in 
        a serverless fashion. Defaults to False
      explainer_serverless: boolean indicating whether to deploy the model in 
        a serverless fashion. Defaults to False
      description: string with the description of the deployment
      example_input: list of example input parameters for the model
      example_output: list of example output for the model
    """
    name: str
    model_serverless = False
    explainer_serverless = False
    description: Optional[str]
    example_input: Optional[List[Any]]
    example_output: Optional[List[Any]]
