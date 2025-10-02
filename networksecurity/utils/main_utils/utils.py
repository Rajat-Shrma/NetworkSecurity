import yaml
from networksecurity.exception.custom_expection import CustomException
from networksecurity.logging.custom_logging import logging

import os, sys
import numpy as np
import dill
import pickle


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


def save_object(file_path: str, obj: object) -> None:
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file:
            dill.dump(file, obj)

    except Exception as e:
        raise CustomException(e, sys)
