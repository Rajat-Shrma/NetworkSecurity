from networksecurity.entity.artifacts_entity import DataIngestionArtifacts,DataValidationArtifacts
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.custom_expection import CustomException
from networksecurity.logging.custom_logging import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.constants import training_pipeline
from networksecurity.utils.main_utils.utils import read_yaml_file,write_yaml_file

from scipy.stats import ks_2samp

import pandas as pd
import numpy as np
import os, sys
class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifacts,
                data_validation_config: DataValidationConfig):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_config=data_validation_config
            self._schema_config=read_yaml_file(training_pipeline.SCHEMA_FILE_PATH)
            
        except Exception as e:
            raise CustomException(e,sys)

    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        return pd.read_csv(file_path)
    
    def validate_number_of_columns(self, dataframe: pd.DataFrame)->bool:
        try:
            number_of_columns=len(self._schema_config['columns'])
            logging.info(f'Required Number Of Columns: {number_of_columns} | The Input Dataframe has {len(dataframe.columns)} columns')

            if len(dataframe.columns)==number_of_columns:
                return True
            return False


        except Exception as e:
            raise CustomException(e,sys)

    def validate_number_of_numeric_columns(self, dataframe: pd.DataFrame)->bool:
        try:
            number_of_numerical_columns=len(self._schema_config['numerical_columns'])
            numerical_col_in_dataframe=0
            for col_name in dataframe.columns:
                if 'int' in str(dataframe[col_name].dtype):
                    numerical_col_in_dataframe+=1
            
            logging.info(f'Required Number Of Numberical Columns: {number_of_numerical_columns} | The Input Dataframe has {numerical_col_in_dataframe} columns')
            return numerical_col_in_dataframe==number_of_numerical_columns


        except Exception as e:
            raise CustomException(e,sys)

    def detect_dataset_drift(self, base_df, current_df, threshold=0.05)->bool:
        try:
            status=True
            report={}
            for column in base_df.columns:
                d1=base_df[column]
                d2=current_df[column]
                is_sample_dist_same=ks_2samp(d1,d2)
                if threshold<=is_sample_dist_same.pvalue:
                    is_found=False
                else:
                    is_found=True
                    status=False
                report.update(
                    {column:{
                    "p_value":float(is_sample_dist_same.pvalue),
                    "drift_status": is_found
                }}
                )
            
            drift_report_file_path=self.data_validation_config.drift_report_file_path
            dir_path=os.path.dirname(drift_report_file_path)
            os.makedirs(dir_path,exist_ok=True)
            write_yaml_file(drift_report_file_path,report)

            return status
        
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_validation(self)->DataValidationArtifacts:
        try:
            train_file_path=self.data_ingestion_artifact.training_path
            test_file_path=self.data_ingestion_artifact.testing_path

            ## read the data from the test and train
            train_dataframe=DataValidation.read_data(train_file_path)
            test_dataframe=DataValidation.read_data(test_file_path)


            total_number_of_train_col_check_status=self.validate_number_of_columns(train_dataframe)

            if not total_number_of_train_col_check_status:
                logging.info("Train dataframe does not contain all columns.")

            total_number_of_test_col_check_status=self.validate_number_of_columns(test_dataframe)
            if not total_number_of_test_col_check_status:
                logging.info("Test dataframe does not contain all columns.")

            numeric_col_train_status=self.validate_number_of_numeric_columns(train_dataframe)

            if not numeric_col_train_status:
                logging.info("Train dataframe does not contain all numeric columns.")

            numeric_col_test_status=self.validate_number_of_numeric_columns(test_dataframe)
            if not numeric_col_test_status:
                logging.info("Test dataframe does not contain all numeric columns.\n")
            
            ## Lets check datadrift
            data_drift_status=self.detect_dataset_drift(train_dataframe,test_dataframe)

            validation_status= total_number_of_test_col_check_status and total_number_of_test_col_check_status and numeric_col_train_status and numeric_col_test_status and data_drift_status
            
            if validation_status:
                dir_path=self.data_validation_config.vaild_data_dir
                os.makedirs(dir_path,exist_ok=True)
                train_dataframe.to_csv(
                    self.data_validation_config.vaild_train_file_path,index=False,header=True
                )

                test_dataframe.to_csv(
                    self.data_validation_config.vaild_test_file_path,index=False,header=True
                )

                return DataValidationArtifacts(
                    validation_status=validation_status,
                    valid_train_file_path=self.data_validation_config.vaild_train_file_path,
                    valid_test_file_path=self.data_validation_config.vaild_test_file_path,
                    invalid_test_file_path='None',
                    invalid_train_file_path='None',
                    drift_report_file_path= self.data_validation_config.drift_report_file_path
                )
            else:
                dir_path=self.data_validation_config.invaild_data_dir
                os.makedirs(dir_path,exist_ok=True)
                train_dataframe.to_csv(
                    self.data_validation_config.invaild_train_file_path,index=False,header=True
                )

                test_dataframe.to_csv(
                    self.data_validation_config.invaild_test_file_path,index=False,header=True
                )

                return DataValidationArtifacts(
                    validation_status=validation_status,
                    valid_train_file_path='None',
                    valid_test_file_path='None',
                    invalid_test_file_path=self.data_validation_config.invaild_test_file_path,
                    invalid_train_file_path=self.data_validation_config.invaild_train_file_path,
                    drift_report_file_path=self.data_validation_config.drift_report_file_path
                )                

        except Exception as e:
            raise CustomException(e,sys)