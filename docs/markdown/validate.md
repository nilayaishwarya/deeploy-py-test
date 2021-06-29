# Validate

This section goes over how to retrieve Predictions of a Deployment and how to validate them.

## Prediction Logs

To see the predictions that have been made, you can retrieve the prediction logs. These can then be used as input for validation requests,
which are explained in the section below.

```python
from deeploy import Client

client_options = {
    'access_key': 'AKIAEXAMPLEKEY',
    'secret_key': 'examplesecretkey',
    'host': 'example.deeploy.ml',
    'workspace_id': 'e7942eeb-3e7e-4d27-a413-23f49a0f24f3',
}
client = Client(**client_options)

logs = client.getLogs('c2bd2a1b-6909-4c42-b3ce-d1d86631e0bf')
```

## Prediction Validation

Validating a prediction means overwriting, or correcting, the model's output. This can be used as a reference, or to be used as training data for a next iteration of the model.

Predictions are validated using a log's ID. These can be retrieved using the method described in the previous section.

```python
from deeploy import Client

client_options = {
    'access_key': 'AKIAEXAMPLEKEY',
    'secret_key': 'examplesecretkey',
    'host': 'example.deeploy.ml',
    'workspace_id': 'e7942eeb-3e7e-4d27-a413-23f49a0f24f3',
}
client = Client(**client_options)

log_id = '6fa9d028-42cc-4074-aa7f-cc93b70f845f'
validation_input = {
    "instances": [
        [39, 7, 1, 1, 1, 1, 4,
         1, 2174, 0, 40, 9]
    ]
}
explanation = 'The model did not take into account the correlation between education level and income.'

client.validate('c2bd2a1b-6909-4c42-b3ce-d1d86631e0bf', log_id, validation_input, explanation)
```
