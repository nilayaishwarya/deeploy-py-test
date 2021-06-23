FROM python:3.9-slim

RUN apt update && apt install git -y

RUN pip3 install pylint flake8