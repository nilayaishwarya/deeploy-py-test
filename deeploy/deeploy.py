import logging
from typing import Optional, List, Any, Callable

from pydantic import BaseModel

from .services import DeeployService, GitService, ModelWrapper, ExplainerWrapper
from .models import Repository, ClientOptions, Deployment
from .enums import PredictionMethod


class Client(object):
    """ 
    A class for interacting with Deeploy
    """

    def __init__(self, options: ClientOptions) -> None:
        """Initialise the Deeploy client
        """
        self.__config = options

        self.__git_service = GitService(self.__config.local_repository_path)
        self.__deeploy_service = DeeployService(
            options.access_key,
            options.secret_key,
            options.host
        )

        if not self.__are_clientoptions_valid(options):
            raise Exception('Client options not valid')

        if not self.__is_git_repository_in_workspace():
            raise Exception(
                'Repository \'%s\' was not found in the Deeploy workspace')

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
        method = PredictionMethod.PREDICT
        description: Optional[str]
        example_input: Optional[List[Any]]
        example_output: Optional[List[Any]]
        model_class_name: Optional[str]

    def deploy(self, model: Any, options: DeployOptions, explainer: Any = None, overwrite: bool = False,
               commit_message: str = None) -> Deployment:
        """Deploy a model on Deeploy

        Parameters
        ----------
        model: Any
          The class instance of an ML model. Supports 
        options: DeployOptions
          The deploy options class containing the deployment options
        explainer: Any, optional
          The class instance of an optional model explainer
        """

        # TODO
        # check if folders are empty or not empty & overwrite

        model_wrapper = ModelWrapper(model)
        if explainer:
            explainer_wrapper = ExplainerWrapper(explainer)

        # TODO
        # empty the model & explainer folder
        # save model & explainer to file system
        # add files to staging area
        # create commit
        # push commit
        # create deployment
        return

    def __are_clientoptions_valid(self, options: ClientOptions) -> bool:
        """Check if the supplied options are valid
        """
        try:
            self.__deeploy_service.get_workspace(options.workspace_id)
        except Exception as e:
            raise e

        return True

    def __is_git_repository_in_workspace(self) -> bool:
        remote_url = self.__git_service.get_remote_url()
        workspace_id = self.__config.workspace_id

        repositories = self.__deeploy_service.get_repositories(workspace_id)
        remote_urls = list(map(lambda x: x.git_ssh_pull_link, repositories))

        if remote_url in remote_urls:
            return True

        return False
