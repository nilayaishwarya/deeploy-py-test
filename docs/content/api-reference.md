# Table of Contents

* [deeploy.deeploy](#deeploy.deeploy)
  * [Client](#deeploy.deeploy.Client)
    * [\_\_init\_\_](#deeploy.deeploy.Client.__init__)
    * [deploy](#deeploy.deeploy.Client.deploy)
* [deeploy.models.deploy\_options](#deeploy.models.deploy_options)
  * [DeployOptions](#deeploy.models.deploy_options.DeployOptions)
    * [name](#deeploy.models.deploy_options.DeployOptions.name)
    * [model\_serverless](#deeploy.models.deploy_options.DeployOptions.model_serverless)
    * [explainer\_serverless](#deeploy.models.deploy_options.DeployOptions.explainer_serverless)
    * [method](#deeploy.models.deploy_options.DeployOptions.method)
    * [description](#deeploy.models.deploy_options.DeployOptions.description)
    * [example\_input](#deeploy.models.deploy_options.DeployOptions.example_input)
    * [example\_output](#deeploy.models.deploy_options.DeployOptions.example_output)
    * [model\_class\_name](#deeploy.models.deploy_options.DeployOptions.model_class_name)
    * [pytorch\_model\_file\_path](#deeploy.models.deploy_options.DeployOptions.pytorch_model_file_path)
* [deeploy.enums.prediction\_method](#deeploy.enums.prediction_method)
  * [PredictionMethod](#deeploy.enums.prediction_method.PredictionMethod)
    * [PREDICT](#deeploy.enums.prediction_method.PredictionMethod.PREDICT)
    * [PREDICT\_PROBA](#deeploy.enums.prediction_method.PredictionMethod.PREDICT_PROBA)

<a name="deeploy.deeploy"></a>
# deeploy.deeploy

<a name="deeploy.deeploy.Client"></a>
## Client Objects

```python
class Client(object)
```

A class for interacting with Deeploy

<a name="deeploy.deeploy.Client.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(access_key: str, secret_key: str, host: str, workspace_id: str, local_repository_path: str, branch_name: str = None) -> None
```

Initialise the Deeploy client

**Arguments**:

- `access_key` _str_ - Personal Access Key generated from the Deeploy UI
- `secret_key` _str_ - Secret Access Key generated from the Deeploy UI
- `host` _str_ - The host at which Deeploy is located, i.e. deeploy.example.com
- `workspace_id` _str_ - The ID of the workspace in which your repository
is located
- `local_repository_path` _str_ - Absolute path to the local git repository
which is connected to Deeploy
- `branch_name` _str, optional_ - The banchname on which to commit new models.
Defaults to the current branchname.

<a name="deeploy.deeploy.Client.deploy"></a>
#### deploy

```python
 | deploy(model: Any, options: DeployOptions, explainer: Any = None, overwrite: bool = False, commit_message: str = None) -> Deployment
```

Deploy a model on Deeploy

**Arguments**:

- `model` _Any_ - The class instance of an ML model
- `options` _DeployOptions_ - An instance of the deploy options class
containing the deployment options
- `explainer` _Any, optional_ - The class instance of an optional model explainer
- `overwrite` _bool, optional_ - Whether or not to overwrite files that are in the 'model' and 'explainer'
folders in the git folder. Defaults to False
- `commit_message` _str, optional_ - Commit message to use

<a name="deeploy.models.deploy_options"></a>
# deeploy.models.deploy\_options

<a name="deeploy.models.deploy_options.DeployOptions"></a>
## DeployOptions Objects

```python
class DeployOptions(BaseModel)
```

Class that contains the options for deploying a model

**Attributes**:

- `name` _str_ - name of the deployment
- `model_serverless` _bool, optional_ - whether to deploy the model in
a serverless fashion. Defaults to False
- `explainer_serverless` _bool, optional_ - whether to deploy the model in
a serverless fashion. Defaults to False
- `method` _PredictionMethod, optional_ - which prediction function to use. Only applicable
to sklearn and xgboost models. Defaults to 'predict'
- `description` _str, optional_ - the description of the deployment
- `example_input` _List, optional_ - list of example input parameters for the model
- `example_output` _List, optional_ - list of example output for the model
- `model_class_name` _str, optional_ - the name of the class containing the
PyTorch model.

<a name="deeploy.models.deploy_options.DeployOptions.name"></a>
#### name

<a name="deeploy.models.deploy_options.DeployOptions.model_serverless"></a>
#### model\_serverless

<a name="deeploy.models.deploy_options.DeployOptions.explainer_serverless"></a>
#### explainer\_serverless

<a name="deeploy.models.deploy_options.DeployOptions.method"></a>
#### method

<a name="deeploy.models.deploy_options.DeployOptions.description"></a>
#### description

<a name="deeploy.models.deploy_options.DeployOptions.example_input"></a>
#### example\_input

<a name="deeploy.models.deploy_options.DeployOptions.example_output"></a>
#### example\_output

<a name="deeploy.models.deploy_options.DeployOptions.model_class_name"></a>
#### model\_class\_name

<a name="deeploy.models.deploy_options.DeployOptions.pytorch_model_file_path"></a>
#### pytorch\_model\_file\_path

<a name="deeploy.enums.prediction_method"></a>
# deeploy.enums.prediction\_method

<a name="deeploy.enums.prediction_method.PredictionMethod"></a>
## PredictionMethod Objects

```python
class PredictionMethod(Enum)
```

<a name="deeploy.enums.prediction_method.PredictionMethod.PREDICT"></a>
#### PREDICT

<a name="deeploy.enums.prediction_method.PredictionMethod.PREDICT_PROBA"></a>
#### PREDICT\_PROBA

