from typing import Optional, List, Any

from pydantic import BaseModel


class DeployOptions(BaseModel):
    """Class that contains the options for deploying a model

    Attributes:
        name (str): name of the deployment
        model_serverless (bool, optional): whether to deploy the model in 
            a serverless fashion. Defaults to False
        explainer_serverless (bool, optional): whether to deploy the model in 
            a serverless fashion. Defaults to False
        description (str, optional): the description of the deployment
        example_input (List, optional): list of example input parameters for the model
        example_output (List, optional): list of example output for the model
    """
    name: str
    model_serverless = False
    explainer_serverless = False
    description: Optional[str]
    example_input: Optional[List[Any]]
    example_output: Optional[List[Any]]
    pytorch_model_file_path: Optional[str]
    pytorch_torchserve_handler_name: Optional[str]
