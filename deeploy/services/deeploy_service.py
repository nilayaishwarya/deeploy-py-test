import base64
import logging
from typing import Optional, List, Any

import requests

from deeploy.models import Deployment, Repository, CreateDeployment
from deeploy.enums import ModelType, ExplainerType, PredictionMethod


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

    def get_repositories(self, workspace_id: str) -> List[Repository]:

        url = '%s/v2/workspaces/%s/repositories?isArchived=false' % (
            self.__host, workspace_id)
        repositories_response = requests.get(
            url, auth=(self.__access_key, self.__secret_key))
        repositories = repositories_response.json()
        return repositories

    def create_deployment(self, workspace_id: str, deployment: CreateDeployment) -> Deployment:
        url = '%s/v2/workspaces/%s/deployments' % (self.__host, workspace_id)
        data = deployment.to_request_body()

        deployment_response = requests.post(
            url, json=data, auth=(self.__access_key, self.__secret_key))
        if self.__request_is_successful(deployment_response):
            logging.info('Deployment created successfully.')
        else:
            raise Exception('Failed to create the deployment.')
        print(deployment_response.json())
        return
