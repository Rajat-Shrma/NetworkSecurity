from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.exception.custom_expection import CustomException
from networksecurity.logging.custom_logging import logging
from networksecurity.entity.config_entity import (
    DataIngestionConfig,
    TrainingPipelineConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig
)
from networksecurity.entity.artifacts_entity import (
    DataIngestionArtifacts,
    DataValidationArtifacts,
    DataTransformationArtifacts,
    ModelTrainerArtifacts
)
import sys

if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        logging.info("Data ingestion Configration Completed")
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        print(data_ingestion_artifact)
        logging.info("Data ingestion Completed")

        logging.info("DataValidation Started.")
        data_validation_config = DataValidationConfig(training_pipeline_config)
        data_validation = DataValidation(
            data_ingestion_artifact, data_validation_config
        )
        data_validation_artifacts = data_validation.initiate_data_validation()
        print(data_validation_artifacts)
        logging.info("Data Validation Completed")

        logging.info("Data Transformation Started")
        data_transformation_config = DataTransformationConfig(training_pipeline_config)
        data_transformation = DataTransformation(
            data_validation_artifact=data_validation_artifacts,
            data_transformation_config=data_transformation_config,
        )
        data_transformation_artifacts = (
            data_transformation.intiate_data_transformation()
        )
        logging.info("Data Transformation completed")
        print(data_transformation_artifacts)

        logging.info("ModelTraining Started")

        model_trainer_config=ModelTrainerConfig(training_pipeline_config=training_pipeline_config)
        model_trainer=ModelTrainer(data_transformation_artifacts=data_transformation_artifacts, model_trainer_config=model_trainer_config)
        model_trainer_artifacts=model_trainer.initiate_model_trainer()
        print(model_trainer_artifacts)
        logging.info('Model Training Compeleted, Best Model Saved!')
    except Exception as e:
        raise CustomException(e, sys)
