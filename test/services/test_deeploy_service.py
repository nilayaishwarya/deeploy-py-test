import pytest
import requests_mock

from deeploy.services import DeeployService
from deeploy.models import Repository, Commit, Deployment, CreateDeployment
from deeploy.enums import ModelType, PredictionMethod, ExplainerType

WORKSPACE_ID = 'abc'

def test__init(deeploy_service):
    with requests_mock.Mocker() as m:
        m.get('https://api.test.deeploy.ml/v2/workspaces')
        assert DeeployService(access_key='abc', secret_key='def', host='test.deeploy.ml')

    with requests_mock.Mocker() as m:
        m.get('https://api.test.deeploy.ml/v2/workspaces', status_code=401)
        with pytest.raises(Exception):
            DeeployService(access_key='abc', secret_key='def', host='test.deeploy.ml')


@pytest.fixture(scope="session")
def deeploy_service():
    with requests_mock.Mocker() as m:
        m.get('https://api.test.deeploy.ml/v2/workspaces')
        return DeeployService(access_key='abc', secret_key='def', host='test.deeploy.ml')


def test__get_repositories(deeploy_service):
    WORKSPACE_ID = 'abc'
    return_object = [
        {
            'id': 'def',
            'name': 'repo 1',
            'status': 1,
            'isArchived': False,
            'workspaceId': WORKSPACE_ID,
            'isPublic': False,
            'gitSSHPullLink': 'git@github.com/example/example.git',
            'createdAt': '2021-03-17T12:55:10.983Z',
            'updatedAt': '2021-03-17T12:55:10.983Z',
            'commits': [],
        }, 
        {
            'id': 'ghi',
            'name': 'repo 2',
            'status': 0,
            'isArchived': False,
            'workspaceId': WORKSPACE_ID,
            'gitSSHPullLink': 'git@gitlab.com/example/example.git',
            'createdAt': '2021-03-17T12:55:10.983Z',
            'updatedAt': '2021-03-17T12:55:10.983Z',
            'commits': [
                {
                    'id': 'jkl',
                    'branchName': 'master',
                    'commit': 'c5f2a21e',
                    'uploadMethod': 0,
                    's3Link': 's3://deeploy-demo/test',
                    'status': 1,
                    'createdAt': '2021-03-17T12:55:10.983Z',
                    'updatedAt': '2021-03-17T12:55:10.983Z',
                },
            ],
        },
    ]
    expected_output = [
        Repository(
            id = 'def',
            name = 'repo 1',
            status = 1,
            isArchived = False,
            workspaceId = WORKSPACE_ID,
            isPublic = False,
            gitSSHPullLink = 'git@github.com/example/example.git',
            createdAt = '2021-03-17T12:55:10.983Z',
            updatedAt = '2021-03-17T12:55:10.983Z',
            commits = [],
        ),
        Repository(
            id = 'ghi',
            name = 'repo 2',
            status = 0,
            isArchived = False,
            workspaceId = WORKSPACE_ID,
            gitSSHPullLink = 'git@gitlab.com/example/example.git',
            createdAt = '2021-03-17T12:55:10.983Z',
            updatedAt = '2021-03-17T12:55:10.983Z',
            commits = [
                Commit(
                    id = 'jkl',
                    branchName = 'master',
                    commit = 'c5f2a21e',
                    uploadMethod = 0,
                    s3Link = 's3://deeploy-demo/test',
                    status = 1,
                    createdAt = '2021-03-17T12:55:10.983Z',
                    updatedAt = '2021-03-17T12:55:10.983Z',
                ),
            ],
        ),
    ]
    with requests_mock.Mocker() as m:
        m.get('https://api.test.deeploy.ml/v2/workspaces/%s/repositories' % WORKSPACE_ID, \
            json=return_object)
        repositories = deeploy_service.get_repositories(WORKSPACE_ID)
        assert repositories == expected_output
        

def test__get_repository(deeploy_service):
    WORKSPACE_ID = 'abc'
    repository_id = 'def'
    return_object = {
        'id': repository_id,
        'name': 'repo 1',
        'status': 1,
        'isArchived': False,
        'workspaceId': WORKSPACE_ID,
        'isPublic': False,
        'gitSSHPullLink': 'git@github.com/example/example.git',
        'createdAt': '2021-03-17T12:55:10.983Z',
        'updatedAt': '2021-03-17T12:55:10.983Z',
        'commits': [],
    }
    expected_output = Repository(
        id = repository_id,
        name = 'repo 1',
        status = 1,
        isArchived = False,
        workspaceId = WORKSPACE_ID,
        isPublic = False,
        gitSSHPullLink = 'git@github.com/example/example.git',
        createdAt = '2021-03-17T12:55:10.983Z',
        updatedAt = '2021-03-17T12:55:10.983Z',
        commits = [],
    )
    with requests_mock.Mocker() as m:
        m.get('https://api.test.deeploy.ml/v2/workspaces/%s/repositories/%s' % (WORKSPACE_ID, repository_id), \
            json=return_object)
        repositories = deeploy_service.get_repository(WORKSPACE_ID, repository_id)
        assert repositories == expected_output


def test__create_deployment(deeploy_service):
    return_object = {
        'commitId': "978b9cd9-f6cf-4f93-83de-ac669046a3e8",
        'createdAt': "2021-03-17T14:59:35.203Z",
        'description': "the first test",
        'explainerServerless': False,
        'explainerType': 4,
        'hasExampleInput': False,
        'id': "63921818-f908-44d6-af72-17e9beef7b6c",
        'inputTensorSize': None,
        'isArchived': False,
        'kfServingId': "x63921818-f908-44d6-af72-17e9beef7b6c",
        'method': "predict",
        'modelClassName': None,
        'modelServerless': False,
        'modelType': 2,
        'name': "client test",
        'outputTensorSize': None,
        'ownerId': "9f39d8b4-b661-43ef-a81f-e8f8dded8c5a",
        'publicURL': "https://api.ute.deeploy.ml/v2/workspaces/e7942eeb-3e7e-4d27-a413-23f49a0f24f3/deployments/63921818-f908-44d6-af72-17e9beef7b6c/predict",
        'repositoryId': "dcd35835-5e5a-4d9a-9116-8732131ed6e2",
        's3Link': "e7942eeb-3e7e-4d27-a413-23f49a0f24f3/repositories/dcd35835-5e5a-4d9a-9116-8732131ed6e2/commits/978b9cd9-f6cf-4f93-83de-ac669046a3e8",
        'stateConfig': {
            'healthy': 14, 
            'affected': 28,
        },
        'status': 1,
        'updatedAt': "2021-03-17T14:59:35.203Z",
        'workspaceId': WORKSPACE_ID,
    }
    expected_output = Deployment(**{
            'commitId': "978b9cd9-f6cf-4f93-83de-ac669046a3e8",
            'createdAt': "2021-03-17T14:59:35.203Z",
            'description': "the first test",
            'explainerServerless': False,
            'explainerType': 4,
            'hasExampleInput': False,
            'id': "63921818-f908-44d6-af72-17e9beef7b6c",
            'inputTensorSize': None,
            'isArchived': False,
            'kfServingId': "x63921818-f908-44d6-af72-17e9beef7b6c",
            'method': "predict",
            'modelClassName': None,
            'modelServerless': False,
            'modelType': 2,
            'name': "client test",
            'outputTensorSize': None,
            'ownerId': "9f39d8b4-b661-43ef-a81f-e8f8dded8c5a",
            'publicURL': "https://api.ute.deeploy.ml/v2/workspaces/e7942eeb-3e7e-4d27-a413-23f49a0f24f3/deployments/63921818-f908-44d6-af72-17e9beef7b6c/predict",
            'repositoryId': "dcd35835-5e5a-4d9a-9116-8732131ed6e2",
            's3Link': "e7942eeb-3e7e-4d27-a413-23f49a0f24f3/repositories/dcd35835-5e5a-4d9a-9116-8732131ed6e2/commits/978b9cd9-f6cf-4f93-83de-ac669046a3e8",
            'stateConfig': {
                'healthy': 14, 
                'affected': 28,
            },
            'status': 1,
            'updatedAt': "2021-03-17T14:59:35.203Z",
            'workspaceId': WORKSPACE_ID,
        }
    )
    with requests_mock.Mocker() as m:
        m.post('https://api.test.deeploy.ml/v2/workspaces/%s/deployments' % WORKSPACE_ID, \
            json=return_object)
        deployment = deeploy_service.create_deployment(WORKSPACE_ID, CreateDeployment(**{
            'repository_id': "dcd35835-5e5a-4d9a-9116-8732131ed6e2",
            'name': "client test",
            'description': "the first test",
            'model_type': ModelType.SKLEARN,
            'method': PredictionMethod.PREDICT,
            'model_serverless': False,
            'explainer_type': ExplainerType.SHAP_KERNEL,
            'explainer_serverless': False,
            'branch_name': 'master',
            'commit_sha': '978b9cd9-f6cf-4f93-83de-ac669046a3e8',
        }))
        assert deployment == expected_output


def test__get_workspace(deeploy_service):
    pass


def test__upload_blob_file(deeploy_service):
    pass
