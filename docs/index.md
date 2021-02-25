# Table of Contents

* [deeploy](#deeploy)
  * [Client](#deeploy.Client)
    * [\_\_init\_\_](#deeploy.Client.__init__)
    * [deploy](#deeploy.Client.deploy)

<a name="deeploy"></a>
# deeploy

<a name="deeploy.Client"></a>
## Client Objects

```python
class Client(object)
```

A class for interacting with Deeploy

<a name="deeploy.Client.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(access_key: str, secret_key: str, host: str, workspace_id: str, local_repository_path: str, branch_name: str = None) -> None
```

Initialise the Deeploy client

<a name="deeploy.Client.deploy"></a>
#### deploy

```python
 | deploy(model: Any, options: DeployOptions, explainer: Any = None, overwrite: bool = False, commit_message: str = None) -> Deployment
```

Deploy a model on Deeploy

Parameters
----------
model: Any
    The class instance of an ML model. Supports 
options: DeployOptions
    The deploy options class containing the deployment options
explainer: Any, optional
    The class instance of an optional model explainer
overwrite: boolean, optional
    Whether or not to overwrite files that are in the 'model' and 'explainer' 
    folders in the git folder. Defaults to False
commit_message: str, optional
    Commit message to use

