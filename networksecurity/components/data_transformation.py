import sys, os
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from networksecurity.constants.training_pipeline import TARGET_COLUMN, DATA_TRANSFORMATION_IMPUTER_PARAMS



from networksecurity.exception.custom_expection import CustomException
from networksecurity.logging.custom_logging import logging
from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.entity.artifacts_entity import DataValidationArtifacts, DataTransformationArtifacts
from networksecurity.utils.main_utils.utils import save_numpy_array, save_object
class DataTransformation:
    def __init__(self, data_validation_artifact: DataValidationArtifacts, data_transformation_config: DataTransformationConfig):
        self.data_validation_artifact=data_validation_artifact
        self.data_transformation_config=data_transformation_config

        

