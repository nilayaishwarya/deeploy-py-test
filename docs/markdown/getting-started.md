# Getting started

## Installation

Download the latest version by running:

```bash
pip3 install deeploy
```

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