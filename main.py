from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.custom_expection import CustomException
from networksecurity.logging.custom_logging import logging
from networksecurity.entity.config_entity import (
    DataIngestionConfig,
    TrainingPipelineConfig,
)
from networksecurity.entity.artifacts_entity import DataIngestionArtifacts
import sys

if __name__ == "__main__":
    try:
        data_ingestion_config = DataIngestionConfig(TrainingPipelineConfig())
        logging.info("Data ingestion Configration Completed")
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info("Data ingestion Completed")

        artifact = data_ingestion.initiate_data_ingestion()

        print(artifact)
    except Exception as e:
        raise CustomException(e, sys)
