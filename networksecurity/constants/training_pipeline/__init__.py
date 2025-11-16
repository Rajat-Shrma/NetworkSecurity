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
TRAINING_BUCKET_NAME='netwrksecurity'
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
        "C": [0.01, 0.1, 1],                # regularization strength
        "penalty": ["l2"],
        "solver": ["liblinear"],             # faster
        "max_iter": [100]
    },

    "gradient_boosting": {
        "n_estimators": [50, 100],           # reduced
        "learning_rate": [0.05, 0.1],
        "max_depth": [3, 5],                 # shallow trees train faster
        "subsample": [1.0]
    },

    "ada_boost": {
        "n_estimators": [50, 100],
        "learning_rate": [0.1, 1.0],
        "algorithm": ["SAMME"]        
    },

    "decision_tree": {
        "criterion": ["gini", "entropy"],
        "max_depth": [5, 10],
        "min_samples_split": [2, 5],
        "min_samples_leaf": [1, 2]
    },

    "svc": {
        "C": [0.1, 1],                       # fewer values
        "kernel": ["linear", "rbf"],         # no poly (too slow)
        "gamma": ["scale"]                   # default, faster
    },

    "knn": {
        "n_neighbors": [3, 5, 7],
        "weights": ["uniform", "distance"],
        "metric": ["euclidean"]              # simpler distance metric
    },

    "naive_bayes": {
        "var_smoothing": [1e-9, 1e-8, 1e-7]
    }
}

