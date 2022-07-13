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
explanation = client.explain(deployment_id, request_body)
```

> **Note:** with the current [pre-build explainer images](https://deeploy-ml.zendesk.com/hc/en-150/articles/4411974086162-Recommended-Framework-Versions) it is not possible to do semi-batch predictions (i.e. multiple predictions per request). See below for a example request body:
> ```
> request_body = {
>    "instances": [
>        [39, 7, 1, 1, 1, 1, 4, 1, 2174, 0, 40, 9],
>        [51, 7, 1, 1, 1, 1, 4, 1, 2174, 0, 40, 8],
>    ]
> }
> ```