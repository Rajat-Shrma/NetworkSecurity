import yaml
from networksecurity.exception.custom_expection import CustomException
from networksecurity.logging.custom_logging import logging

import os, sys
import numpy as np
import dill
import pickle

from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV


def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)

    except Exception as e:
        raise CustomException(e, sys)


def write_yaml_file(file_path, content):
    try:
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise CustomException(e, sys)


def save_numpy_array(file_path: str, array: np.array):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file:
            np.save(file, array)

    except Exception as e:
        raise CustomException(e, sys)


def load_numpy_array(file_path: str):
    try:

        with open(file_path, "rb") as file:
            return np.load(file)

    except Exception as e:
        raise CustomException(e, sys)


def save_object(file_path: str, obj: object) -> None:
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file:
            dill.dump(obj=obj, file=file)

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path: str) -> object:
    try:
        with open(file_path, 'rb') as file:
            return dill.load(file)

    except Exception as e:
        raise CustomException(e, sys)


def get_models_report(
    x_train: np.array,
    y_train: np.array,
    x_test: np.array,
    y_test: np.array,
    models: dict,
    params: dict,
) -> dict:
    models_report = {}
    best_models = {}
    for model_name, model in models.items():
        parameters = params[model_name]
        grid = GridSearchCV(model, param_grid=parameters, cv=3)

        grid.fit(x_train, y_train)

        best_model = grid.best_estimator_

        y_test_pred = best_model.predict(x_test)

        best_model_accuracy = accuracy_score(y_pred=y_test_pred, y_true=y_test)

        models_report[model_name] = best_model_accuracy
        best_models[model_name] = best_model
        logging.info(f'{model_name} Done!')

    return models_report, best_models
