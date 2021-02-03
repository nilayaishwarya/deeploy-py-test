from typing import Optional, List, Any

from pydantic import BaseModel

from .git_service import GitService, GitServiceOptions
from .models import Repository, ClientOptions

class Client(object):
  """ 
  A class for interacting with Deeploy
  """

  def __init__(self, options: ClientOptions) -> None:
    """Initialise the Deeploy client
    """
    if not self.__are_clientoptions_valid(options):
      raise 'Client options not valid'

    self.__config = options
    git_options: GitClientOptions = {
      "local_repository_path": self.__config.local_repository_path,
    }
    self.__git_client = GitClient(git_options)
    self.__deeploy_client = 

    if not self.__is_git_repository_in_workspace():
      raise 'Repository \'%s\' was not found in the Deeploy workspace'

    if not self.__user_has_deploy_permissions_in_workspace():
      raise 'User does not have deploy permissions in the workspace'
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

  def __are_clientoptions_valid(self, options: ClientOptions) -> bool:
    """Check if the supplied options are valid
    """
    # TODO: 
    # verify access keys
    # verify workspace existence
    # verify workspace permissions (deploy model)
    # verify repository is contained in workspace
    return False

  def __is_git_repository_in_workspace(self) -> bool:
    remote_url = self.__git_client.get_remote_url()
    workspace_id = self.__config.workspace_id
    return False

  def __user_has_deploy_permissions_in_workspace(self) -> bool:
    return False