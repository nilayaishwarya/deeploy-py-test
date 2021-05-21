import base64
import logging
from typing import Optional, List, Any
import os

import requests
from pydantic import parse_obj_as

from deeploy.models import Deployment, Repository, CreateDeployment, Workspace, V1Prediction, V2Prediction
from deeploy.enums import ModelType, ExplainerType, PredictionVersion


class DeeployService(object):
    """ 
    A class for interacting with the Deeploy API
    """

    def __init__(self, access_key: str, secret_key: str, host: str, insecure=False) -> None:
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__host = 'http://api.%s' % host if insecure else 'https://api.%s' % host

        if not self.__keys_are_valid():
            raise Exception('Access keys are not valid')
        return

    def get_repositories(self, workspace_id: str) -> List[Repository]:
        url = '%s/v2/workspaces/%s/repositories' % (
            self.__host, workspace_id)
        params = {
            'isArchived': False,
        }

        repositories_response = requests.get(
            url, params=params, auth=(self.__access_key, self.__secret_key))

        repositories = parse_obj_as(
            List[Repository], repositories_response.json())

        return repositories

    def get_repository(self, workspace_id: str, repository_id: str) -> Repository:
        url = '%s/v2/workspaces/%s/repositories/%s' % (
            self.__host, workspace_id, repository_id)

        repository_response = requests.get(
            url, auth=(self.__access_key, self.__secret_key))
        if not self.__request_is_successful(repository_response):
            raise Exception('Repository does not exist in the workspace.')

        repository = parse_obj_as(Repository, repository_response.json())

        return repository

    def create_deployment(self, workspace_id: str, deployment: CreateDeployment) -> Deployment:
        url = '%s/v2/workspaces/%s/deployments' % (self.__host, workspace_id)
        data = deployment.to_request_body()

        deployment_response = requests.post(
            url, json=data, auth=(self.__access_key, self.__secret_key))
        if not self.__request_is_successful(deployment_response):
            raise Exception('Failed to create the deployment: %s' % str(deployment_response.json()) )

        deployment = parse_obj_as(
            Deployment, deployment_response.json())

        return deployment

    def get_workspace(self, workspace_id: str) -> Workspace:
        url = '%s/v2/workspaces/%s' % (self.__host, workspace_id)

        workspace_response = requests.get(
            url, auth=(self.__access_key, self.__secret_key))
        if not self.__request_is_successful(workspace_response):
            raise Exception('Workspace does not exist.')

        workspace = parse_obj_as(Workspace, workspace_response.json())

        return workspace

    def upload_blob_file(self, local_file_path: str, relative_folder_path: str, workspace_id: str, repository_id: str, uuid: str) -> str:
        url = '%s/v2/workspaces/%s/repositories/%s/upload' % (self.__host, workspace_id, repository_id)
        params = {
            'commitSha': uuid,
            'folderPath': relative_folder_path,
        }
        files = { 'file': open(local_file_path, 'rb') }
        r = requests.post(url, files=files, params=params, auth=(self.__access_key, self.__secret_key))
        blob_storage_path = r.json()['data']['referencePath']
        return blob_storage_path

    def predict(self, workspace_id: str, deployment_id: str, request_body: dict) -> V1Prediction or V2Prediction:
        url = '%s/v2/workspaces/%s/deployments/%s/predict' % (self.__host, workspace_id, deployment_id)

        prediction_response = requests.post(
            url, json=request_body, auth=(self.__access_key, self.__secret_key))
            
        if not self.__request_is_successful(prediction_response):
            raise Exception('Failed to call predictive model.')
        prediction = self.__parse_prediction(prediction_response)
        return prediction


    def explain(self, workspace_id: str, deployment_id: str, request_body: dict, image: bool = False) -> object:
        url = '%s/v2/workspaces/%s/deployments/%s/explain' % (self.__host, workspace_id, deployment_id)
        params = {
            'image': str(image).lower(),
        }

        explanation_reponse = requests.post(
            url, json=request_body, params=params, auth=(self.__access_key, self.__secret_key))
        if not self.__request_is_successful(explanation_reponse):
            raise Exception('Failed to call explainer model.')
        explanation = explanation_reponse.json()
        return explanation

    def __keys_are_valid(self) -> bool:
        host_for_testing = '%s/v2/workspaces' % self.__host
        workspaces_response = requests.get(
            host_for_testing, auth=(self.__access_key, self.__secret_key))
        if self.__request_is_successful(workspaces_response):
            return True
        return False

    def __request_is_successful(self, request: requests.Response) -> bool:
        if str(request.status_code)[0] == '2':
            return True
        return False

    def __check_prediction_version(self, prediction_response: dict) -> PredictionVersion:
        if 'predictions' in prediction_response.json():
             return PredictionVersion.V1
        else:
            return PredictionVersion.V2

    def __parse_prediction(self, prediction_response: dict) -> V1Prediction or V2Prediction:
        if self.__check_prediction_version(prediction_response) == PredictionVersion.V1:
             prediction = parse_obj_as(
                V1Prediction, prediction_response.json())
        else:
            prediction = parse_obj_as(
                V2Prediction, prediction_response.json())
        return prediction
