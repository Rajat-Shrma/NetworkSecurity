from networksecurity.exception.custom_expection import CustomException
from networksecurity.logging.custom_logging import logging
from networksecurity.constants import training_pipeline
from networksecurity.entity.artifacts_entity import DataIngestionArtifacts
## Data ingestion Configration

from networksecurity.entity.config_entity import DataIngestionConfig

import pandas as pd
import numpy as np
import os
import sys
from typing import List
from pymongo import MongoClient

from sklearn.model_selection import train_test_split
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e, sys)

    def export_collection_as_dataframe(self):
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongo_client = MongoClient(MONGO_DB_URL)
            collection = self.mongo_client[database_name][collection_name]

            logging.info('Data reading from mongo db. Done.')

            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.tolist():
                df = df.drop(columns=["_id"], axis=1)

            df.replace({"na": np.nan}, inplace=True)
            return df
        except Exception as e:
            raise CustomException(e, sys)

    def export_data_into_feature_store(self, dataframe: pd.DataFrame):
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            feature_store_dir = os.path.dirname(feature_store_file_path)
            os.makedirs(feature_store_dir, exist_ok=True)
            dataframe.to_csv(feature_store_file_path, index=False, header=True)

            logging.info('raw data file saved.')
        except Exception as e:
            raise CustomException(e, sys)
        

    def split_data_into_train_test(self,dataframe: pd.DataFrame):
        try:
            logging.info('Train Test Split Begin.')
            train_set,test_set=train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio, random_state=2)

            training_file_path=self.data_ingestion_config.training_file_path
            test_file_path=self.data_ingestion_config.testing_file_path

            os.makedirs(os.path.dirname(training_file_path), exist_ok=True)
            train_set.to_csv(training_file_path, index=False,header=True)
            logging.info('Train Set Saved.')
            os.makedirs(os.path.dirname(test_file_path), exist_ok=True)
            test_set.to_csv(test_file_path, index=False,header=True)
            logging.info('Test Set Saved.')


        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_collection_as_dataframe()
            self.export_data_into_feature_store(dataframe)
            self.split_data_into_train_test(dataframe)
            
            data_ingestion_artifact=DataIngestionArtifacts(training_path=self.data_ingestion_config.training_file_path,testing_path=self.data_ingestion_config.testing_file_path)
            
            return data_ingestion_artifact
            

        except Exception as e:
            raise CustomException(e, sys)
