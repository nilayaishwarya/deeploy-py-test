from typing import Optional, List, Any

from pydantic import BaseModel

from deeploy.models.model_reference_json import BlobReference, DockerReference


class DeployOptions(BaseModel):
    """Class that contains the options for deploying a model
    """  # noqa

    name: str
    """str: name of the deployment"""  # noqa
    model_serverless = False
    """bool, optional: whether to deploy the model in a serverless fashion. Defaults to False"""  # noqa
    model_instance_type: Optional[str]
    """str, optional: The preferred instance type for the model pod."""  # noqa
    model_cpu_limit: Optional[float]
    """float, optional: CPU limit of model pod, in CPUs."""  # noqa
    model_cpu_request:  Optional[float]
    """float, optional: CPU request of model pod, in CPUs."""  # noqa
    model_mem_limit: Optional[int]
    """int, optional: RAM limit of model pod, in Megabytes."""  # noqa
    model_mem_request: Optional[int]
    """int, optional: RAM request of model pod, in Megabytes."""  # noqa
    explainer_serverless = False
    """bool, optional: whether to deploy the model in a serverless fashion. Defaults to False"""  # noqa
    explainer_instance_type: Optional[str]
    """str, optional: The preferred instance type for the model pod."""  # noqa
    explainer_cpu_limit: Optional[float]
    """float, optional: CPU limit of model pod, in CPUs."""  # noqa
    explainer_cpu_request:  Optional[float]
    """float, optional: CPU request of model pod, in CPUs."""  # noqa
    explainer_mem_limit: Optional[int]
    """int, optional: RAM limit of model pod, in Megabytes."""  # noqa
    explainer_mem_request: Optional[int]
    """int, optional: RAM request of model pod, in Megabytes."""  # noqa
    description: Optional[str]
    """str, optional: the description of the deployment"""  # noqa
    example_input: Optional[List[Any]]
    """List, optional: list of example input parameters for the model"""  # noqa
    example_output: Optional[List[Any]]
    """List, optional: list of example output for the model"""  # noqa
    feature_labels: Optional[List[str]]
    """List, optional: list of feature labels for the explanations"""  # noqa
    pytorch_model_file_path: Optional[str]
    """str, optional: absolute or relative path to the .py file containing the pytorch model class definition"""  # noqa
    pytorch_torchserve_handler_name: Optional[str]
    """str, optional: TorchServe handler name. One of
        ['image_classifier', 'image_segmenter', 'object_detector', 'text_classifier'].
        See the [TorchServe documentation](https://github.com/pytorch/serve/blob/master/docs/default_handlers.md#torchserve-default-inference-handlers)
        for more info."""  # noqa
    modelDockerConfig: Optional[DockerReference] = None
    """DockerReference: docker configuration object of the model"""  # noqa
    modelBlobConfig: Optional[BlobReference] = None
    """BlobReference: blob configuration object of the explainer"""  # noqa
    explainerDockerConfig: Optional[DockerReference] = None
    """DockerReference: docker configuration object of the explainer"""  # noqa
    explainerBlobConfig: Optional[BlobReference] = None
    """BlobReference: blob configuration object of the explainer"""  # noqa
    prediction_method: Optional[int] = None
    """str: Whether to use predict (0) or predict_proba (1) for SKLearn and XGBoost deployments.""" # noqa
    custom_id: Optional[str] = None
    """str: Name of the custom id"""
