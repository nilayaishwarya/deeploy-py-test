from typing import Optional, List, Any

from pydantic import BaseModel

class Client(object):
  """ 
  A class for interacting with Deeploy
  """

  class ClientOptions(BaseModel):
    """
    Class containing the Deeploy client options

    Attributes:
      access_key: string representing the personal access key
      secret_key: string representing the personal secret key
      host: string representing the domain on which Deeploy is hosted
      workspace_id: string representing the workspace id in which to create
        deployments
      local_repository_path: string representing the relative or absolute path
        to the local git repository
      branch_name: string representing the branch name on which to commit. Defaults
        to the local active branch
    """
    access_key: str
    secret_key: str
    host: str
    workspace_id: str
    local_repository_path: str
    branch_name: Optional[str]

  def __init__(self, options: ClientOptions) -> None:
    """Initialise the Deeploy client
    """
    return

  class DeployOptions(BaseModel):
    """
    Class that contains the options for deploying a model
    
    Attributes:
      name: name of the deployment
      model_serverless: boolean indicating whether to deploy the model in 
        a serverless fashion. Defaults to False
      explainer_serverless: boolean indicating whether to deploy the model in 
        a serverless fashion. Defaults to False
      method: string indication which prediction function to use. Only applicable
        to sklearn and xgboost models. Defaults to 'predict'
      description: string with the description of the deployment
      example_input: list of example input parameters for the model
      example_output: list of example output for the model
      model_class_name: string indicating the name of the class containing a 
        PyTorch model.
    """
    name: str
    model_serverless = False
    explainer_serverless = False
    method = 'predict'
    description: Optional[str]
    example_input: Optional[List[Any]]
    example_output: Optional[List[Any]]
    model_class_name: Optional[str]

  def deploy(self, model_class: Any, options: DeployOptions, explainer_class: Any = None) -> None:
    """Deploy a model on Deeploy

    Parameters
    ----------
    model_class: Any
      The class instance of an ML model. Supports 
    options: DeployOptions
      The deploy options class containing the deployment options
    explainer_class: Any, optional
      The class instance of an optional model explainer
    """
    return