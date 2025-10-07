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

class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config=TrainingPipelineConfig()
    
    def perform_data_ingestion(self)-> DataIngestionArtifacts:
        try:
            logging.info('Data Ingestion Started.')
            self.data_ingestion_config= DataIngestionConfig(self.training_pipeline_config)
            data_ingestion=DataIngestion(self.data_ingestion_config)
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logging.info('Data Ingestion Completed.')
            return data_ingestion_artifact
        
        except Exception as e:
            raise CustomException(e,sys)



    
    def perform_data_validation(self, data_ingestion_artifact: DataIngestionArtifacts)-> DataValidationArtifacts:
        try:
            logging.info('Data Validation Started.')
            self.data_validation_config=DataValidationConfig(self.training_pipeline_config)
            data_validation=DataValidation(data_validation_config=self.data_validation_config, data_ingestion_artifact=data_ingestion_artifact)
            data_validation_artifacts=data_validation.initiate_data_validation()
            logging.info('Data Validation Completed.')
            return data_validation_artifacts
        
        except Exception as e:
            raise CustomException(e,sys)

    def perform_data_transformation(self, data_validation_artifacts)-> DataTransformationArtifacts:
        try:

            logging.info('Data Transformation Started.')
            self.data_transformation_config=DataTransformationConfig(self.training_pipeline_config)
            data_transformation=DataTransformation(data_validation_artifacts, self.data_transformation_config)
            data_transformation_artifacts=data_transformation.intiate_data_transformation()
            logging.info('Data Transformation Completed.')
            return data_transformation_artifacts

        except Exception as e:
            raise CustomException(e,sys)
    
    def perform_model_training(self, data_transformation_artifacts: DataTransformationArtifacts)-> ModelTrainerArtifacts:
        try:

            logging.info('Model Training Started.')
            self.model_trainer_config=ModelTrainerConfig(training_pipeline_config=self.training_pipeline_config)
            model_trainer=ModelTrainer(data_transformation_artifacts=data_transformation_artifacts,model_trainer_config=self.model_trainer_config)
            model_trainer_artifacts=model_trainer.initiate_model_trainer()
            logging.info('Model Training Completed.')
            return model_trainer_artifacts

        except Exception as e:
            raise CustomException(e,sys)
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact=self.perform_data_ingestion()
            data_validation_artifacts=self.perform_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifacts=self.perform_data_transformation(data_validation_artifacts=data_validation_artifacts)
            model_trainer_artifacts=self.perform_model_training(data_transformation_artifacts=data_transformation_artifacts)
            
            return model_trainer_artifacts
        except Exception as e:
            raise CustomException(e,sys)
        
                                                



        

