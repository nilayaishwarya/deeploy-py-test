from typing import Optional, Dict, Any

from pydantic import BaseModel

from deeploy.models.create_deployment import CreateVersion


class UpdateDeployment(BaseModel):
    """Class that contains the options for updating a model
    """  # noqa
    deployment_id: str
    name: Optional[str]
    kfserving_id: Optional[str]
    owner_id: Optional[str]
    public_url: Optional[str]
    description: Optional[str]
    status: Any
    updating_to: Optional[CreateVersion]

    def to_request_body(self) -> Dict:
        request_body = {
            'name': self.name,
            'kfServingId': self.kfserving_id,
            'ownerId': self.owner_id,
            'description': self.description,
            'status': self.status,
            'updatingTo': {
                'commit': self.updating_to.commit,
                'commitMessage': self.updating_to.commit_message,
                'hasExampleInput': self.updating_to.has_example_input,
                'exampleInput': self.updating_to.example_input,
                'exampleOutput': self.updating_to.example_output,
                'inputTensorSize': self.updating_to.input_tensor_size,
                'outputTensorSize': self.updating_to.output_tensor_size,
                'modelType': self.updating_to.model_type,
                'modelServerless': self.updating_to.model_serverless,
                'explainerType': self.updating_to.explainer_type,
                'explainerServerless': self.updating_to.explainer_serverless,
            }
        }
        request_body['updatingTo'] = {k: v for k, v in request_body['updatingTo'].items()
                                      if v is not None}
        return {k: v for k, v in request_body.items() if v is not None and v != {}}
