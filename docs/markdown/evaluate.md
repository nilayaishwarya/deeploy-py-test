# Evaluate

This section goes over how to retrieve Predictions of a Deployment and how to evaluate them.

## Prediction Logs

To see the predictions that have been made, you can retrieve the prediction logs. These can then be used as input for evaluation requests,
which are explained in the section below.

```python
from deeploy import Client

workspace_id = 'e7942eeb-3e7e-4d27-a413-...'
deployment_id = 'c2bd2a1b-6909-4c42-b3ce-...'

client_options = {
    'deployment_token': 'exampletoken',
    # evaluating is currenly only
    # supported with the token auth method
    'host': 'example.deeploy.ml',
    'workspace_id': workspace_id,
}

client = Client(**client_options)

request_body = {
    "instances": []
}

explanation = client.explain(deployment_id, request_body)

request_log_id=explanation['requestLogId']
prediction_log_id=explanation['predictionLogIds'][0]

prediction_log = client.getOneRequestLog(deployment_id, request_log_id, prediction_log_id)
```

## Prediction Evaluation

Evaluating a prediction means overwriting, or correcting, the model's output. This can be used as a reference, or to be used as training data for a next iteration of the model.

Predictions are evaluated using a log's ID. These can be retrieved using the method described in the previous section.

```python
evaluation_input = {
    "result": 1,
    "value": {"predictions": [False]},
    "explanation": "example"
}

client.evaluate(deployment_id, request_log_id, prediction_log_id, evaluation_input)
```
