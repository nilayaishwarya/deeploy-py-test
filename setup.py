import setuptools

setuptools.setup(
    name='deeploy',
    version='0.0.2',
    description='The official Deeploy client for Python.',
    author='Lars Suanet',
    author_email='lars@deeploy.ml',
    packages=setuptools.find_packages(),
    install_requires=[
        "pydantic>=1.7.3",
        "gitpython>=3.1.12",
        "requests>=2.25.1",
        "joblib>=1.0.1",
        "dill>=0.3.3",
        "ipython>=7.20.0",
        "nbconvert>=6.0.7",
        "pyyaml==5.4.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)