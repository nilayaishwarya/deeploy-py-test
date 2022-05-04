# Getting started

## Installation

Download the latest version by running:

```bash
pip3 install deeploy
```

## Deploy flows

There are multiple paths that can be followed in order to create a new deployment.

`Model and explainer variables (*)`
When passing a model and/or explainer to the deploy function the client will update the reference.json files in the repository or create new reference.json files if they do not yet exist.

```
from deeploy import DeployOptions
from deeploy.enums import ModelType

deploy_options = DeployOptions(**{
        'name': 'My Deployment Name',
        'description': 'My Deployment Description'
    })
    
client.deploy(
    options=deploy_options, 
    overwrite=True, 
    model_type=ModelType.PYTORCH.value, 
    local_repository_path='myPath', 
    model=myPytorchModel)
```

`Blob storage locations and custom Docker images (*)`
By passing access credentials to a blob storage location or Docker image it is possible to upload models and explainers that are stored as a file in a blob storage location or as a custom Docker image. This approach will update the reference.json files in the repository or create new reference.json files if they do not yet exist.

```
from deeploy import DeployOptions
from deeploy.enums import ModelType

deploy_options = DeployOptions(**{
        'modelBlobReferenceUrl': myUrl,
    })

client.deploy(
    options=deploy_options, 
    overwrite=True, 
    model_type=ModelType.PYTORCH.value, 
    local_repository_path='myPath',
    )
```

`Existing reference.json files`
Creating a deployment from existing reference.json files requires passing a model and/or explainer type unless it is a custom Docker image.

```
from deeploy import DeployOptions
from deeploy.enums import ModelType

deploy_options = DeployOptions(**{
        'name': 'My Deployment Name',
        'description': 'My Deployment Description'
    })

client.deploy(
    options=deploy_options, 
    model_type=ModelType.PYTORCH.value, 
    local_repository_path='myPath')
```

*Only possible when the argument `overwrite` is set to True, otherwise the client will use the existing reference.json files to create the deployment.

## Deploying a model

Initialise the `Client`:

```python
from deeploy import Client, DeployOptions

client_options = {
    'access_key': 'AKIAEXAMPLEKEY',
    'secret_key': 'examplesecretkey',
    'host': 'example.deeploy.ml',
    'workspace_id': 'e7942eeb-3e7e-4d27-a413-23f49a0f24f3',
}
client = Client(**client_options)
```

Train a model and explainer

```python
import sklearn
import shap

# prepare the dataset
X,y = shap.datasets.adult()
X_display,y_display = shap.datasets.adult(display=True)
X_train, X_valid, y_train, y_valid = sklearn.model_selection.train_test_split(X, y, test_size=0.2, random_state=7)

# train the model
knn = sklearn.neighbors.KNeighborsClassifier()
knn.fit(X_train, y_train)

# create the explainer
f = lambda x: knn.predict_proba(x)[:,1]
med = X_train.median().values.reshape((1,X_train.shape[1]))
explainer = shap.KernelExplainer(f, med)
```

And finally, deploy the model and explainer on Deeploy:

```python
deploy_options = {
    'model': knn, 
    'options': DeployOptions(**{
        'name': 'Client example',
        'model_serverless': False,
        'explainer_serverless': True,
        'description': 'This is an example model deployed with the Python client',
    }), 
    'explainer': explainer,
    'overwrite': True,
}
client.deploy(**deploy_options)
```