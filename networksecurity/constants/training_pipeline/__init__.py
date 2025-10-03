import os
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import (
    GradientBoostingClassifier,
    AdaBoostClassifier,
)
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

"""
Constants variables for training
"""

TARGET_COLUMN: str = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str = "Artifacts"
RAWDATA_FILE_NAME: str = "raw.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")

"""
Data ingestion related constants starts with DATA_INGESTION VAR NAME
"""

DATA_INGESTION_DATABASE_NAME: str = "NETWORKSECURITY"
DATA_INGESTION_COLLECITON_NAME: str = "NETWORKSECURITYDATA"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2

"""
Data validation related constants starts with DATA_VALIDATION VAR NAME
"""

DATA_VALIDATION_DIR: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"


"""
Data Transformation related constants starts with DATA_TRANSFORMATION VAR NAME
"""

DATA_TRANSFORMATION_DIR: str = "data_transformation"
DATA_TRANSFORMATION_DATA_DIR: str = "transformed"
DATA_TRANSFORMATON_TRAIN_FILE_NAME: str = "train.npy"
DATA_TRANSFORMATION_TEST_FILE_NAME: str = "test.npy"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_obj"
DATA_TRANSFORMATION_OBJECT_FILE_NAME: str = "preprocessor.pkl"
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}

"""
Model Trainer related constants starts with MODEL_TRAINER VAR NAME
"""

MODEL_TRAINER_DIR: str = "madel_trainer"
MODEL_TRAINER_MODEL_FILE_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_ACCURACY: float = 0.6
MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD: float = 0.05

MODEL_TRAINER_DICT_OF_MODEL_TO_TEST: dict = {
    "logistic_regression": LogisticRegression(),
    "gradient_boosting": GradientBoostingClassifier(),
    "ada_boost": AdaBoostClassifier(),
    "decision_tree": DecisionTreeClassifier(),
    "svc": SVC(),
    "knn": KNeighborsClassifier(),
    "naive_bayes": GaussianNB(),
}

MODEL_TRAINER_PARAMS: dict = {
    "logistic_regression": {
        "C": [0.1],  # regularization strength
        "penalty": ["l2"],
    },
    "gradient_boosting": {
        "learning_rate": [0.01],  # shrinkage rate
        "n_estimators": [50],
    },
    "ada_boost": {"n_estimators": [50, 100]},
    "decision_tree": {"max_depth": [10]},
    "svc": {"C": [0.1], "kernel": ["rbf"]},
    "knn": {"n_neighbors": [5]},
    "naive_bayes": {},  # No major params for GaussianNB
}
