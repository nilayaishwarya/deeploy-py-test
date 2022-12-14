import pytest
import requests_mock

from deeploy.services import DeeployService
from deeploy.models import Repository, Deployment, CreateDeployment, V1Prediction, V2Prediction, RequestLog, PredictionLog, RequestLogs
from deeploy.enums import ModelType, ExplainerType

WORKSPACE_ID = 'abc'


def test__init(deeploy_service):
    with requests_mock.Mocker() as m:
        m.get('https://api.test.deeploy.ml/workspaces')
        assert DeeployService(host='test.deeploy.ml', workspace_id='ghi',
                              access_key='abc', secret_key='def')

    with requests_mock.Mocker() as m:
        m.get('https://api.test.deeploy.ml/workspaces', status_code=401)
        with pytest.raises(Exception):
            DeeployService(host='test.deeploy.ml', workspace_id='ghi',
                           access_key='abc', secret_key='def')


@pytest.fixture(scope="session")
def deeploy_service():
    with requests_mock.Mocker() as m:
        m.get('https://api.test.deeploy.ml/workspaces')
        return DeeployService(host='test.deeploy.ml', workspace_id='ghi', access_key='abc', secret_key='def')


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
            'remotePath': 'git@github.com/example/example.git',
            'createdAt': '2021-03-17T12:55:10.983Z',
            'updatedAt': '2021-03-17T12:55:10.983Z',
        },
        {
            'id': 'ghi',
            'name': 'repo 2',
            'status': 0,
            'isArchived': False,
            'workspaceId': WORKSPACE_ID,
            'remotePath': 'git@gitlab.com/example/example.git',
            'createdAt': '2021-03-17T12:55:10.983Z',
            'updatedAt': '2021-03-17T12:55:10.983Z',
        },
    ]
    expected_output = [
        Repository(
            id='def',
            name='repo 1',
            status=1,
            isArchived=False,
            workspaceId=WORKSPACE_ID,
            isPublic=False,
            remotePath='git@github.com/example/example.git',
            createdAt='2021-03-17T12:55:10.983Z',
            updatedAt='2021-03-17T12:55:10.983Z',
        ),
        Repository(
            id='ghi',
            name='repo 2',
            status=0,
            isArchived=False,
            workspaceId=WORKSPACE_ID,
            remotePath='git@gitlab.com/example/example.git',
            createdAt='2021-03-17T12:55:10.983Z',
            updatedAt='2021-03-17T12:55:10.983Z',
        ),
    ]
    with requests_mock.Mocker() as m:
        m.get('https://api.test.deeploy.ml/workspaces/%s/repositories' % WORKSPACE_ID,
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
        'remotePath': 'git@github.com/example/example.git',
        'createdAt': '2021-03-17T12:55:10.983Z',
        'updatedAt': '2021-03-17T12:55:10.983Z',
    }
    expected_output = Repository(
        id=repository_id,
        name='repo 1',
        status=1,
        isArchived=False,
        workspaceId=WORKSPACE_ID,
        isPublic=False,
        remotePath='git@github.com/example/example.git',
        createdAt='2021-03-17T12:55:10.983Z',
        updatedAt='2021-03-17T12:55:10.983Z',
    )
    with requests_mock.Mocker() as m:
        m.get('https://api.test.deeploy.ml/workspaces/%s/repositories/%s' % (WORKSPACE_ID, repository_id),
              json=return_object)
        repositories = deeploy_service.get_repository(WORKSPACE_ID, repository_id)
        assert repositories == expected_output


def test__create_deployment(deeploy_service):
    return_object = {
        'createdAt': "2021-03-17T14:59:35.203Z",
        'description': "the first test",
        'id': "63921818-f908-44d6-af72-17e9beef7b6c",
        'isArchived': False,
        'kfServingId': "x63921818-f908-44d6-af72-17e9beef7b6c",
        'name': "client test",
        'ownerId': "9f39d8b4-b661-43ef-a81f-e8f8dded8c5a",
        'publicURL': "https://api.ute.deeploy.ml/workspaces/e7942eeb-3e7e-4d27-a413-23f49a0f24f3/deployments/63921818-f908-44d6-af72-17e9beef7b6c/predict",
        'status': 1,
        'updatedAt': "2021-03-17T14:59:35.203Z",
        'workspaceId': WORKSPACE_ID,
    }
    expected_output = Deployment(**{
        'createdAt': "2021-03-17T14:59:35.203Z",
        'description': "the first test",
        'hasExampleInput': False,
        'id': "63921818-f908-44d6-af72-17e9beef7b6c",
        'isArchived': False,
        'kfServingId': "x63921818-f908-44d6-af72-17e9beef7b6c",
        'name': "client test",
        'ownerId': "9f39d8b4-b661-43ef-a81f-e8f8dded8c5a",
        'publicURL': "https://api.ute.deeploy.ml/workspaces/e7942eeb-3e7e-4d27-a413-23f49a0f24f3/deployments/63921818-f908-44d6-af72-17e9beef7b6c/predict",
        'status': 1,
        'updatedAt': "2021-03-17T14:59:35.203Z",
        'workspaceId': WORKSPACE_ID,
    }
    )
    with requests_mock.Mocker() as m:
        m.post('https://api.test.deeploy.ml/workspaces/%s/deployments' % WORKSPACE_ID,
               json=return_object)
        deployment = deeploy_service.create_deployment(WORKSPACE_ID, CreateDeployment(**{
            'name': "client test",
            'description': "the first test",
            'updating_to': {
                'repository_id': "dcd35835-5e5a-4d9a-9116-8732131ed6e2",
                'model_type': ModelType.SKLEARN,
                'model_serverless': False,
                'explainer_type': ExplainerType.SHAP_KERNEL,
                'explainer_serverless': False,
                'branch_name': 'master',
                'commit': '978b9cd9-f6cf-4f93-83de-ac669046a3e8',
            }
        }))
        assert deployment == expected_output


def test__get_workspace(deeploy_service):
    pass


def test__upload_blob_file(deeploy_service):
    pass


def test_predict(deeploy_service):
    # TODO: add tests for V2 predictions
    request_body = {
        "instances": [
            [6.8,  2.8,  4.8,  1.4],
            [6.0,  3.4,  4.5,  1.6]
        ]
    }
    return_object_V1 = {
        "predictions": [
            {
                "scores": [0.999114931, 9.20987877e-05, 0.000136786213, 0.000337257545, 0.000300532585, 1.84813616e-05],
                "prediction": 0,
                "key": "1"
            }
        ]
    }
    expected_output_V1 = V1Prediction(
        **{
            "predictions": [
                {
                    "scores": [0.999114931, 9.20987877e-05, 0.000136786213, 0.000337257545, 0.000300532585, 1.84813616e-05],
                    "prediction": 0,
                    "key": "1"
                }
            ]
        })

    with requests_mock.Mocker() as m:
        m.post('https://api.test.deeploy.ml/workspaces/%s/deployments/%s/predict' % (WORKSPACE_ID, '20c2593d-e09d-4246-be84-46f81a40a7d4'),
               json=return_object_V1)
        prediction = deeploy_service.predict(
            workspace_id=WORKSPACE_ID, deployment_id='20c2593d-e09d-4246-be84-46f81a40a7d4', request_body=request_body)
        assert prediction == expected_output_V1

    with requests_mock.Mocker() as m:
        m.post('https://api.test.deeploy.ml/workspaces/%s/deployments/%s/predict' % (WORKSPACE_ID, '20c2593d-e09d-4246-be84-46f81a40a7d4'),
               status_code=400)
        with pytest.raises(Exception):
            deeploy_service.predict(
                workspace_id=WORKSPACE_ID, deployment_id='20c2593d-e09d-4246-be84-46f81a40a7d4', request_body=request_body)


def test_explain(deeploy_service):
    request_body = {
        "inputs": [
            {
                "name": "input-0",
                "shape": [2, 4],
                "datatype": "FP32",
                "data": [
                    [6.8, 2.8, 4.8, 1.4],
                    [6.0, 3.4, 4.5, 1.6]
                ]
            }
        ]
    }

    with requests_mock.Mocker() as m:
        m.post('/workspaces/%s/deployments/%s/explain' % (WORKSPACE_ID, '20c2593d-e09d-4246-be84-46f81a40a7d4'),
               json=request_body)
        assert deeploy_service.explain(
            workspace_id=WORKSPACE_ID, deployment_id='20c2593d-e09d-4246-be84-46f81a40a7d4', request_body=request_body, image=True)

    with requests_mock.Mocker() as m:
        m.post('/workspaces/%s/deployments/%s/explain' % (WORKSPACE_ID, '20c2593d-e09d-4246-be84-46f81a40a7d4'),
               status_code=400)
        with pytest.raises(Exception):
            deeploy_service.explain(
                workspace_id=WORKSPACE_ID, deployment_id='20c2593d-e09d-4246-be84-46f81a40a7d4', request_body=request_body, image=True)


def test_getRequestLogs(deeploy_service):
    return_object = {
        "data": [
            {"id": "bac4848a-e7bd-4af6-821d-2e384dc016cc",
             "deploymentId": "ccadb1a1-9036-418c-9936-3f7ac6c4ec8c",
             "commit": "4c1a62d",
             "requestContentType": "application/json",
             "responseTimeMS": 26,
             "statusCode": 500,
             "tokenId": "b6d8c781-2526-4e03-9b43-4c1a62d064db",
             "createdAt": "2021-05-06T15:36:07.597Z",
             "predictionLogs": {}}], "count": 1
    }

    expected_output = RequestLogs(
        **{"data": [
            RequestLog(
                **{"id": "bac4848a-e7bd-4af6-821d-2e384dc016cc",
                   "deploymentId": "ccadb1a1-9036-418c-9936-3f7ac6c4ec8c",
                   "commit": "4c1a62d",
                   "requestContentType": "application/json",
                   "responseTimeMS": 26,
                   "statusCode": 500,
                   "tokenId": "b6d8c781-2526-4e03-9b43-4c1a62d064db",
                   "createdAt": "2021-05-06T15:36:07.597Z",
                   "predictionLogs": {}})],
            "count": 1})

    with requests_mock.Mocker() as m:
        m.get('https://api.test.deeploy.ml/workspaces/%s/deployments/%s/requestLogs' % (WORKSPACE_ID, '20c2593d-e09d-4246-be84-46f81a40a7d4'),
              json=return_object)
        logs = deeploy_service.getRequestLogs(workspace_id=WORKSPACE_ID,
                                              deployment_id='20c2593d-e09d-4246-be84-46f81a40a7d4')
        assert logs == expected_output

    with requests_mock.Mocker() as m:
        m.get('https://api.test.deeploy.ml/workspaces/%s/deployments/%s/requestLogs' % (WORKSPACE_ID, '20c2593d-e09d-4246-be84-46f81a40a7d4'),
              status_code=400)
        with pytest.raises(Exception):
            deeploy_service.getRequestLogs(workspace_id=WORKSPACE_ID,
                                           deployment_id='20c2593d-e09d-4246-be84-46f81a40a7d4')


def test_getOnePredictionLog(deeploy_service):
    return_object = {
        "id": "bac4848a-e7bd-4af6-821d-2e384dc016cc",
        "requestBody": {},
        "requestBodyBlobLink": '',
        "responseBody": {},
        "requestLog": {},
        "evaluation": {},
        "actual": {},
        "createdAt": "2021-05-06T15:36:07.597Z",
        "tags": {'primary': None, 'secondary': []}
    }

    expected_output = PredictionLog(
        **{ "id": "bac4848a-e7bd-4af6-821d-2e384dc016cc",
            "requestBody": {},
            "requestBodyBlobLink": '',
            "responseBody": {},
            "requestLog": {},
            "evaluation": {},
            "actual": {},
            "createdAt": "2021-05-06T15:36:07.597Z",
            "tags": {'primary': None, 'secondary': []}})

    with requests_mock.Mocker() as m:
        m.get('https://api.test.deeploy.ml/workspaces/%s/deployments/%s/requestLogs/%s/predictionLogs/%s' % (WORKSPACE_ID, '20c2593d-e09d-4246-be84-46f81a40a7d4', 'abc', 'abc'),
              json=return_object)
        log = deeploy_service.getOnePredictionLog(
            workspace_id=WORKSPACE_ID, deployment_id='20c2593d-e09d-4246-be84-46f81a40a7d4', request_log_id='abc', prediction_log_id='abc')
        assert log == expected_output

    with requests_mock.Mocker() as m:
        m.get('https://api.test.deeploy.ml/workspaces/%s/deployments/%s/requestLogs/%s/predictionLogs/%s' % (WORKSPACE_ID, '20c2593d-e09d-4246-be84-46f81a40a7d4', 'abc', 'abc'),
              status_code=400)
        with pytest.raises(Exception):
            deeploy_service.getOnePredictionLog(
                workspace_id=WORKSPACE_ID, deployment_id='20c2593d-e09d-4246-be84-46f81a40a7d4', request_log_id='abc', prediction_log_id='abc')


def test_evaluate(deeploy_service: DeeployService):
    with requests_mock.Mocker() as m:
        m.post("https://api.test.deeploy.ml/workspaces/%s/deployments/%s/requestLogs/%s/predictionLogs/%s/evaluations" % (WORKSPACE_ID, '20c2593d-e09d-4246-be84-46f81a40a7d4', 'abc', 'abc'),
               status_code=401)
        with pytest.raises(Exception):
            deeploy_service.evaluate(
                workspace_id='abc', deployment_id='20c2593d-e09d-4246-be84-46f81a40a7d4', request_log_id='abc', prediction_log_id='abc', evaluation_input={})
