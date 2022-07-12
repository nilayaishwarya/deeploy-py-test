# Infer

The Python client can make predictions and get explanations for a certain deployment.

## Predict & Explain

```python
from deeploy import Client

workspace_id = 'e7942eeb-3e7e-4d27-a413-...'
deployment_id = 'c2bd2a1b-6909-4c42-b3ce-...'

client_options = {
    'access_key': 'AKIAEXAMPLEKEY',
    'secret_key': 'examplesecretkey',
    'host': 'example.deeploy.ml',
    'workspace_id': workspace_id,
}
client = Client(**client_options)

request_body = {
    "instances": [
        [39, 7, 1, 1, 1, 1, 4,
         1, 2174, 0, 40, 9]
    ]
}

prediction = client.predict(deployment_id, request_body)
explanation = client.predict(deployment_id, request_body)
```
