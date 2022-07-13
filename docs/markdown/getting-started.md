# Getting started

## Installation

Download the latest version by running:

```bash
pip install deeploy
```


## Initializing the Deeploy python client
In order to initialize the Python client you need a [personal key pair](https://deeploy-ml.zendesk.com/hc/en-150/articles/6505862346386-Personal-key-pairs) (account level access) or [deployment API token](https://deeploy-ml.zendesk.com/hc/en-150/articles/360021070580-Integrating-a-Deployment) (deployment level access), the domain of you Deeploy installation and a [workspace id](https://deeploy-ml.zendesk.com/knowledge/articles/360019010659/en-150?brand_id=360002003940&return_to=%2Fhc%2Fen-150%2Farticles%2F360019010659). You will need your Deeploy installation to retrieve these details.

Use the following code to initialise the Deeploy `Client`:

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

## Model and explainer Frameworks
Deeploy support the following model frameworks with pre-build model and explainer images to make mode deployments easy:
- **Models**
  - [Scikit-Learn](https://pypi.org/project/scikit-learn/0.20.3/)
  - [XGBoost](https://pypi.org/project/xgboost/0.82/)
  - [LightGBM](https://pypi.org/project/lightgbm/2.3.1/)
  - [PyTorch](https://pypi.org/project/torch/1.3.1/)
  - [Tensorflow](https://pypi.org/project/tensorflow/2.2.2/)
- **Explainers**
  - [Anchors](https://pypi.org/project/alibi/0.4.0/)
  - [Shap Kernel](https://pypi.org/project/shap/0.36.0/)

For more information see [here](https://deeploy-ml.zendesk.com/hc/en-150/articles/4411974086162-Recommended-Framework-Versions)

Next to prebuild images Deeploy also support custom model and explainer images. For more information about custome Docker deployments we recommend to start [here](https://deeploy-ml.zendesk.com/hc/en-150/articles/4406047508370-Deploying-Custom-Docker-Images). In the depoy section of the documentation an example is shown.

## Up next
The Python client currently includes the following functionality:
- [Create and update deployments](deploy.md)
- [Request predictions and explanations from a deployment API](infer.md)
- [Evaluate predictions](evaluate.md)
- [Submit actuals for predictions](actuals.md)


For more infromation about authentication check this [section](auth.md)
