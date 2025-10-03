from datetime import datetime
import os
from networksecurity.constants import training_pipeline


class TrainingPipelineConfig:
    def __init__(self, timestamp=datetime.now()):
        self.timestamp = timestamp.strftime("%m_%d_%Y_%M_%S")
        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.artifacts_name = training_pipeline.ARTIFACT_DIR
        self.artifacts_dir = os.path.join(self.artifacts_name, self.timestamp)


class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_ingestion_dir: str = os.path.join(
            training_pipeline_config.artifacts_dir,
            training_pipeline.DATA_INGESTION_DIR_NAME,
        )

        self.feature_store_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_FEATURE_STORE,
            training_pipeline.RAWDATA_FILE_NAME,
        )

        self.training_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTED_DIR,
            training_pipeline.TRAIN_FILE_NAME,
        )

        self.testing_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTED_DIR,
            training_pipeline.TEST_FILE_NAME,
        )

        self.train_test_split_ratio: float = (
            training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        )

        self.database_name = training_pipeline.DATA_INGESTION_DATABASE_NAME
        self.collection_name = training_pipeline.DATA_INGESTION_COLLECITON_NAME


class DataValidationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_validation_dir: str = os.path.join(
            training_pipeline_config.artifacts_dir,
            training_pipeline.DATA_VALIDATION_DIR,
        )
        self.vaild_data_dir: str = os.path.join(
            self.data_validation_dir, training_pipeline.DATA_VALIDATION_VALID_DIR
        )
        self.invaild_data_dir: str = os.path.join(
            self.data_validation_dir, training_pipeline.DATA_VALIDATION_INVALID_DIR
        )

        self.vaild_train_file_path: str = os.path.join(
            self.vaild_data_dir, training_pipeline.TRAIN_FILE_NAME
        )
        self.invaild_train_file_path: str = os.path.join(
            self.invaild_data_dir, training_pipeline.TRAIN_FILE_NAME
        )

        self.vaild_test_file_path: str = os.path.join(
            self.vaild_data_dir, training_pipeline.TEST_FILE_NAME
        )
        self.invaild_test_file_path: str = os.path.join(
            self.invaild_data_dir, training_pipeline.TEST_FILE_NAME
        )

        self.drift_report_file_path: str=os.path.join(
            self.data_validation_dir,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME
        )

class DataTransformationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.training_pipeline_config=training_pipeline_config

        self.data_transformation_dir: str=os.path.join(training_pipeline_config.artifacts_dir,training_pipeline.DATA_TRANSFORMATION_DIR)
        self.data_transformation_data_dir: str=os.path.join(self.data_transformation_dir,training_pipeline.DATA_TRANSFORMATION_DATA_DIR)
        self.transformed_train_data_file_path: str=os.path.join(self.data_transformation_data_dir,training_pipeline.DATA_TRANSFORMATON_TRAIN_FILE_NAME)
        self.transformed_test_data_file_path: str=os.path.join(self.data_transformation_data_dir,training_pipeline.DATA_TRANSFORMATION_TEST_FILE_NAME)
        self.transformed_object_file_path: str=os.path.join(self.data_transformation_dir,training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,training_pipeline.DATA_TRANSFORMATION_OBJECT_FILE_NAME)


class ModelTrainerConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.model_trainer_dir=os.path.join(training_pipeline_config.artifacts_dir, training_pipeline.MODEL_TRAINER_DIR)
        self.model_path=os.path.join(self.model_trainer_dir, training_pipeline.MODEL_TRAINER_MODEL_FILE_NAME)
        self.models_to_test: dict= training_pipeline.MODEL_TRAINER_DICT_OF_MODEL_TO_TEST
        self.models_params: dict= training_pipeline.MODEL_TRAINER_PARAMS
        self.model_expected_accuracy: float= training_pipeline.MODEL_TRAINER_EXPECTED_ACCURACY
        self.model_overfitting_underfitting_threshold=training_pipeline.MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD

        