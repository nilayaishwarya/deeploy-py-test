# Authentication

There are two methods of authenticating with the Deeploy Python client. These are Personal Access Keys and Deployment Tokens. Both methods give different levels of access to Deeploy.

## Personal Access Keys

Personal Access Keys are generated from the **Account** section of the Deeploy UI. The use of these keys allows for access to all the functionalities that would otherwise be available to you in the UI, including `deploy`, `predict` and `explain`.

These keys should only be used by the person that generated them, not by any applications. For that we use Deployment Tokens.

The client can be initialised using these keys like so:

```python
from deeploy import Client

client_options = {
    'access_key': 'AKIAEXAMPLEKEY',
    'secret_key': 'examplesecretkey',
    'host': 'example.deeploy.ml',
    'workspace_id': 'e7942eeb-3e7e-4d27-a413-23f49a0f24f3',
}
client = Client(**client_config)
```

## Deployment Tokens

Deployment Tokens are generated from the **Integration** tab of a single Deployment. Deployment Tokens allow you (or your application) access to all functionalties related to the Deployment it is connected to, including `predict`, `explain` and `evaluate`.

Deployment Tokens are to be used by applications that consume predictions/explanations from a Deployment or that need to update a Deployment.

The client can be initialised using a Deployment Token like so:

```python
client_options = {
    'deployment_token': 'exampledeploymenttoken',
    'host': 'example.deeploy.ml',
    'workspace_id': 'e7942eeb-3e7e-4d27-a413-23f49a0f24f3',
}
client = Client(**client_config)
```
