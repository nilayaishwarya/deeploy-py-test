# Actuals

This section goes over how to retrieve Predictions of a Deployment and how to submit actuals for them for Deeploy to calculate performance metrics based on it.

## Prediction Logs

To see the predictions that have been made, you can retrieve the prediction logs. These can then be used as input for evaluation requests,
which are explained in the section below.

```python
from deeploy import Client

workspace_id = 'e7942eeb-3e7e-4d27-a413-...'
deployment_id = 'c2bd2a1b-6909-4c42-b3ce-...'

client_options = {
    'deployment_token': 'exampletoken',
    # submitting actuals is currenly only
    # supported with the token auth method
    'host': 'example.deeploy.ml',
    'workspace_id': workspace_id,
}

client = Client(**client_options)

prediction_logs = client.getRequestLogs(deployment_id)
```

## Submit actuals for prediction logs

By submitting actions you add labels to prediction made in the past. This can be used as a reference, or to be used as training data for a next iteration of the model.

In order to submit actuals you will be using a prediction log IDs. These can be retrieved using the method described in the previous section.

```python
actuals_input = {
  "predictionIds": [
    prediction_logs.data[0].id,
    prediction_logs.data[1].id,
    prediction_logs.data[2].id,
    prediction_logs.data[3].id
  ],
  "actualValues": [
    {"predictions": [False]},
    {"predictions": [True]},
    {"predictions": [True]},
    {"predictions": [False]}
  ]
}

client.actuals(deployment_id, actuals_input)
```