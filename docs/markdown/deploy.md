# Deploy and update
## Deploy flows
There are multiple routes that can be followed in order to create or update a new deployment. Below a schematic overview is shown of the available scenarios from the Deeploy client.

<p align="left">
    <img align="left" src="https://deeploy-ml.gitlab.io/deeploy-python-client/img/deeploy-routes.png" width="250px" />
</p>

### Preparation
In order to deploy models, you need Personal Access Keys. For more information regarding authentication, see [Authentication](https://deeploy-ml.gitlab.io/deeploy-python-client/authentication/).

Another part of the preparation is gettin familiar with the repository contract that Deeploy uses, you can find more information about that [here](https://deeploy-ml.zendesk.com/hc/en-150/articles/4411887195666-Preparing-a-repository).

### Route 1: Deploy from existing reference.json
Creating a deployment or updating from existing reference.json files requires passing a model and/or explainer type unless it is a custom Docker image.

**Create deployment**
- See [here](https://deeploy-ml.gitlab.io/deeploy-python-client/api-reference/#deeploy.models.deploy_options) for all update arguments.
- See [here](https://deeploy-ml.gitlab.io/deeploy-python-client/api-reference/#deploy) for all update arguments.
```
from deeploy import DeployOptions
from deeploy.enums import ModelType

deploy_options = DeployOptions(**{
        'name': 'My Deployment Name',
        'description': 'My Deployment Description'
    })

# create new deployment
client.deploy(
    options=deploy_options,
    overwrite=False,
    model_type=ModelType.PYTORCH.value,
    local_repository_path='myPath')
```

**Update**
- See [here](https://deeploy-ml.gitlab.io/deeploy-python-client/api-reference/#deeploy.models.update_options) for all update arguments.
- See [here](https://deeploy-ml.gitlab.io/deeploy-python-client/api-reference/#update) for all update arguments.
```
from deeploy import UpdateOptions
from deeploy.enums import ModelType

update_options = UpdateOptions(**{
        'name': 'My Deployment Name',
        'description': 'My Deployment Description'
    })

# create new deployment
client.update(
    options=update_options,
    overwrite=False,
    model_type=ModelType.PYTORCH.value,
    local_repository_path='myPath')
```

### Route 2: Point to a storage lation in object storage or Docker registry and let Deeploy generate a reference.json for you.
This approach will update the reference.json files in the repository or create new reference.json files if they do not yet exist.

**Create deployment**
- See [here](https://deeploy-ml.gitlab.io/deeploy-python-client/api-reference/#deeploy.models.model_reference_json) for all blob reference arguments.
```
from deeploy import DeployOptions, BlobReference
from deeploy.enums import ModelType

# Create Blob reference
model_reference = BlobReference(**{
    'url': 's3://deeploy-examples/pytorch/agenet/model'
})

deploy_options = DeployOptions(**{
        'name': 'My Deployment Name',
        'description': 'My Deployment Description'
        'modelBlobConfig': model_reference,
    })

client.deploy(
    options=deploy_options,
    overwrite=True,
    model_type=ModelType.PYTORCH.value,
    local_repository_path='myPath',
    )
```

*Custom docker deployment*
```
from deeploy import DeployOptions, BlobReference
from deeploy.enums import ModelType

# Create Blob reference
model_reference = DockerReference(**{
    'image': 'docker.io/example/image:1.2.3'
    'uri': '/model:predict'
    'port': 8000
})

deploy_options = DeployOptions(**{
        'name': 'My Deployment Name',
        'description': 'My Deployment Description'
        'modelBlobConfig': model_reference,
    })

client.deploy(
    options=deploy_options,
    overwrite=True,
    model_type=ModelType.CUSTOM.value,
    local_repository_path='myPath',
    )
```
**Update**
```
from deeploy import UpdateOptions, BlobReference
from deeploy.enums import ModelType

# Create Blob reference
model_reference = BlobReference(**{
    'url': 's3://deeploy-examples/pytorch/agenet/model'
})

deploy_options = DeployOptions(**{
        'name': 'My Deployment Name',
        'description': 'My Deployment Description'
        'modelBlobConfig': model_reference,
    })

client.deploy(
    options=deploy_options,
    overwrite=True,
    model_type=ModelType.PYTORCH.value,
    local_repository_path='myPath',
    )
```
*Custom docker deployment*
```
from deeploy import UpdateOptions, DockerReference
from deeploy.enums import ModelType

# Create Blob reference
model_reference = DockerReference(**{
    'image': 'docker.io/example/image:1.2.3'
    'uri': '/model:predict'
    'port': 8000
})

deploy_options = DeployOptions(**{
        'name': 'My Deployment Name',
        'description': 'My Deployment Description'
        'modelBlobConfig': model_reference,
    })

client.deploy(
    options=deploy_options,
    overwrite=True,
    model_type=ModelType.CUSTOM.value,
    local_repository_path='myPath',
    )
```

### Route 3: Deploy in memory model
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


## Creating multiple deployments from a monorepo using the Deeploy contract path (Route 1)
Deeploy supports creating multiple deployments from the same repository using a contract path. The contract path is the path relative to the root of a repository where the [deeploy contract](https://deeploy-ml.zendesk.com/hc/en-150/articles/4411887195666-Preparing-a-repository) for a deployment is located. The idea is that you create your Deeploy contract path at a subfolder in the repository, as shown in the example below.

```
repository
|
|_subfolder_1
|  |_ model
|  |   |_ reference.json
|  |_ explainer
|  |   |_ reference.json
|  |_ metadata.json
|
|_subfolder_2
   |_ model
       |_ reference.json
```
To create a deployment from a contract path, you provide the relative path from the repository root as input to the Python SDK or Core API. In the example above "subfolder_1" or "subfolder_2".
```
from deeploy import DeployOptions
from deeploy.enums import ModelType

deploy_options = DeployOptions(**{
        'name': 'My Deployment Name',
        'description': 'My Deployment Description'
    })

# create new deployment
client.deploy(
    options=deploy_options,
    overwrite=False,
    model_type=ModelType.PYTORCH.value,
    local_repository_path='myPath'
    contract_path='subfolder_1')
```

Check out the [API reference](api-reference.md) for more information.
