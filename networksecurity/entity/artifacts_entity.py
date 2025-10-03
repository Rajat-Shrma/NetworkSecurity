from dataclasses import dataclass


@dataclass
class DataIngestionArtifacts:
    training_path: str
    testing_path: str


@dataclass
class DataValidationArtifacts:
    validation_status: str
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str
    invalid_test_file_path: str
    drift_report_file_path: str


@dataclass
class DataTransformationArtifacts:
    transformed_object_file_path: str
    transformed_train_file_path: str
    transformed_test_file_path: str


@dataclass
class ClassificationMetricArtifacts:
    f1_score: float
    precision_score: float
    recall_score: float


@dataclass
class ModelTrainerArtifacts:
    trained_model_path: str
    trained_metric_artifacts: ClassificationMetricArtifacts
    test_metric_artifacts: ClassificationMetricArtifacts
