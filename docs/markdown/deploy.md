# Deploy

In order to deploy models, you need Personal Access Keys. For more information regarding authentication, see [Authentication](./configuration.md#authentication).

## Model Frameworks

Deeploy supports a number of ML model frameworks. Below you'll find these frameworks and any
framework-specific steps to deploying a model using the client.

### Scikit-learn

Deeploy currently supports Scikit-learn models up to version `0.20.3`. We are working to upgrade this to a more recent version.

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

Deeploy currently supports XGBoost models up to version `0.82`. We are working to upgrade this to a more recent version.

```python
...
import xgboost as xgb
from sklearn.datasets import load_iris
import os

iris = load_iris()
y = iris['target']
X = iris['data']
dtrain = xgb.DMatrix(X, label=y)
param = {
    'max_depth': 6,
    'eta': 0.1,
    'silent': 1,
    'nthread': 4,
    'num_class': 10,
    'objective': 'multi:softmax',
}
xgb_model = xgb.train(params=param, dtrain=dtrain)

deploy_options = DeployOptions(**{
    'name': 'Iris classifier',
    'model_serverless': False,
    'description': 'This model classifies a flower species based on the flower properties.',
})
client.deploy(xgb_model, deploy_options, './iris-project', overwrite=True)
```

### TensorFlow

```python
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import Conv1D, GlobalMaxPooling1D
from tensorflow.keras.datasets import imdb

max_features = 5000
maxlen = 400
batch_size = 32
embedding_dims = 50
filters = 250
kernel_size = 3
hidden_dims = 250
epochs = 2

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)

model = Sequential()
# we start off with an efficient embedding layer which maps
# our vocab indices into embedding_dims dimensions
model.add(Embedding(max_features,
                    embedding_dims,
                    input_length=maxlen))
model.add(Dropout(0.2))

# we add a Convolution1D, which will learn filters
# word group filters of size filter_length:
model.add(Conv1D(filters,
                 kernel_size,
                 padding='valid',
                 activation='relu',
                 strides=1))
# we use max pooling:
model.add(GlobalMaxPooling1D())

# We add a vanilla hidden layer:
model.add(Dense(hidden_dims))
model.add(Dropout(0.2))
model.add(Activation('relu'))

# We project onto a single unit output layer, and squash it with a sigmoid:
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          validation_data=(x_test, y_test))
```

### PyTorch

```python
...
import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

transform = transforms.Compose(
    [transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                        download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                            shuffle=True, num_workers=2)

testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                        download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=4,
                                            shuffle=False, num_workers=2)

classes = ('plane', 'car', 'bird', 'cat',
            'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

net = Net()

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

for epoch in range(2):  # loop over the dataset multiple times

    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        # get the inputs; data is a list of [inputs, labels]
        inputs, labels = data

        # zero the parameter gradients
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        # print statistics
        running_loss += loss.item()
        if i % 2000 == 1999:    # print every 2000 mini-batches
            print('[%d, %5d] loss: %.3f' %
                    (epoch + 1, i + 1, running_loss / 2000))
            running_loss = 0.0
print('Finished Training')

deploy_options = DeployOptions(**{
    'name': 'Pytorch Cifar10',
    'model_serverless': False,
    'description': 'Pytorch model trained on the cifar10 dataset.',
})
client.deploy(net, deploy_options, './cifar10', overwrite=True)
```

## Explainer Frameworks

### Alibi

From the Alibi open-source explainer module, Deeploy supports `AnchorTabular`, `AnchorImage` and `AnchorText`.

```python
from tensorflow.keras.applications.inception_v3 import InceptionV3
from alibi.datasets import fetch_imagenet
from alibi.explainers import AnchorImage

model = InceptionV3(weights='imagenet')

predict_fn = lambda x: model.predict(x)

segmentation_fn = 'slic'
kwargs = {'n_segments': 15, 'compactness': 20, 'sigma': .5}
image_shape = (299, 299, 3)
explainer = AnchorImage(predict_fn, image_shape, segmentation_fn=segmentation_fn, segmentation_kwargs=kwargs, images_background=None)

explainer.predict_fn = None # Clear explainer predict_fn as its a lambda and will be reset when loaded

deploy_options = DeployOptions(**{
    'name': 'InceptionV3 explained',
    'model_serverless': False,
    'explainer_serverless': False,
    'description': 'InceptionV3 with an Alibi AnchorImage explainer.',
})
client.deploy(model, deploy_options, './inceptionv3', overwrite=True,
              explainer, overwrite=True)
```

### SHAP

Deeploy currently supports the KernelExplainer for the SHAP explainer framework.

#### KernelExplainer

```python
...
import sklearn
import shap
import dill
import joblib


X,y = shap.datasets.adult()
X_display,y_display = shap.datasets.adult(display=True)
X_train, X_valid, y_train, y_valid = sklearn.model_selection.train_test_split(X, y, test_size=0.2, random_state=7)

knn = sklearn.neighbors.KNeighborsClassifier()
knn.fit(X_train, y_train)

f = lambda x: knn.predict_proba(x)[:,1]
med = X_train.median().values.reshape((1,X_train.shape[1]))
explainer = shap.KernelExplainer(f, med)

deploy_options = DeployOptions(**{
    'name': 'KNN with SHAP',
    'model_serverless': False,
    'explainer_serverless': True,
    'description': "This is a KNN model built on the adult dataset. \
        It also contains a SHAP KernelExplainer.",
})
client.deploy(knn, deploy_options, './iris-project', overwrite=True)
```
