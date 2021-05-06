# Deploy

## Model Frameworks

Deeploy supports a number of ML model frameworks. Below you'll find these frameworks and any 
framework-specific steps to deploying a model using the client.

### Scikit-learn

```python
...
from sklearn import svm
from sklearn import datasets

# load the MNIST dataset
digits = datasets.load_digits()

# train a SVM on the dataset
clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(digits.data[:-1], digits.target[:-1])

# deploy the model on Deeploy
deploy_options = DeployOptions(**{
    'name': 'MNIST model',
    'model_serverless': True,
    'description': 'This model predicts an integer 0-9 from a 32x32 grayscale image.',
})
client.deploy(clf, deploy_options, './mnist-project', overwrite=True)
```

### XGBoost

```python

```

### TensorFlow

```python

```

### PyTorch

```python

```

## Explainer Frameworks

### Alibi

### SHAP