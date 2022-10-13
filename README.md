# Deep CNN Classifier Project

## workflow

1. Update config.yaml 
2. Update secrets.yaml [optional] # if you have any then only
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config.
6. Update the components
7. Update the pipelines
8. Test run pipeline stage
9. Run tox for testing your package
10. Update the dvc.yaml
11. run "dvc repro" for running all the stages in pipeline

![img](https://raw.githubusercontent.com/AmitSingh-DataScientist/Deep_CNN_Classifier/main/docs/images/Data%20Ingestion%402x%20(1).png)


STEP 1: Set the env variable | Get it from Dagshub -> remote tab -> mlflow tab
MLFLOW_TRACKING_URI=https://dagshub.com/AmitSingh-DataScientist/Deep_CNN_Classifier.mlflow \
MLFLOW_TRACKING_USERNAME=AmitSingh-DataScientist \
MLFLOW_TRACKING_PASSWORD=<> \

STEP 2: Install mlflow

STPE 3: Set remote URI

STEP 4: Use context manager to mlflow to start run and then log metrics, params, and model

## Docker related command and informaion
FROM python:3.8-slim    # download pyton image with bare minimum requirement of os to run

WORKDIR /app            # create app folder inside root directory

COPY . .                # copy all the files in app folder

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py"]


Run this in terminal

export DOCKER_BUILDKIT=0
export COMPOSE_DOCKER_CLI_BUILD=0

This will fix that error and you will be able to build your docker image.


## Sample data for testing-
https://raw.githubusercontent.com/c17hawke/raw_data/main/sample_data.zip