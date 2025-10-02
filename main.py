from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.custom_expection import CustomException
from networksecurity.logging.custom_logging import logging
from networksecurity.entity.config_entity import (
    DataIngestionConfig,
    TrainingPipelineConfig,
    DataValidationConfig
)
from networksecurity.entity.artifacts_entity import DataIngestionArtifacts,DataValidationArtifacts
import sys

if __name__ == "__main__":
    try:
        training_pipeline_config=TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        logging.info("Data ingestion Configration Completed")
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        print(data_ingestion_artifact)
        logging.info("Data ingestion Completed")

        logging.info('DataValidation Started.')
        data_validation_config=DataValidationConfig(training_pipeline_config)
        data_validation=DataValidation(data_ingestion_artifact,data_validation_config)
        data_validation_artifacts=data_validation.initiate_data_validation()

        print(data_validation_artifacts)
    except Exception as e:
        raise CustomException(e, sys)
