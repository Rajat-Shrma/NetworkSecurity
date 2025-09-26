import os
import sys
import json
import certifi
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
ca = certifi.where()

from networksecurity.exception.custom_expection import CustomException
from networksecurity.logging.custom_logging import logging


MONGO_DB_URL = os.getenv("MONGO_DB_URL")


class DataExtract:
    def __init__(self, file_path):
        try:

            self.data = pd.read_csv(file_path)

        except Exception as e:
            raise CustomException(e, sys)

    def csv_to_json_converter(self):
        try:
            self.data.reset_index(drop=True, inplace=True)
            records = list(json.loads(self.data.T.to_json()).values())
            return records
        except Exception as e:
            raise CustomException(e, sys)

    def insert_data_to_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            self.mongodb_client = MongoClient(MONGO_DB_URL)

            self.database = self.mongodb_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(records)

            return len(self.records)

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE = "NETWORKSECURITY"
    COLLECTION = "NETWORKSECURITYDATA"
    networkobj = DataExtract(FILE_PATH)

    records = networkobj.csv_to_json_converter()
    print(records)
    print(networkobj.insert_data_to_mongodb(records, DATABASE, COLLECTION))
