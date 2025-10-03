import sys, os
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from networksecurity.constants.training_pipeline import TARGET_COLUMN, DATA_TRANSFORMATION_IMPUTER_PARAMS



from networksecurity.exception.custom_expection import CustomException
from networksecurity.logging.custom_logging import logging
from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.entity.artifacts_entity import DataValidationArtifacts, DataTransformationArtifacts
from networksecurity.utils.main_utils.utils import save_numpy_array, save_object
class DataTransformation:
    def __init__(self, data_validation_artifact: DataValidationArtifacts, data_transformation_config: DataTransformationConfig):
        try:
            self.data_validation_artifact=data_validation_artifact
            self.data_transformation_config=data_transformation_config

            if self.data_validation_artifact.validation_status:
                pass
            else:
                raise CustomException('You Do Not Have Valid Data')
            

        except Exception as e:
            raise CustomException(e,sys)
        
    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise CustomException(e,sys)
        
    def get_data_transformer_object(self)->Pipeline:
        logging.info('Enter get_data_transformer_object method of transformation class')

        try:
            imputer=KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            preprocessor=Pipeline([
                ('imputer',imputer)
            ])

            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)

    def intiate_data_transformation(self)-> DataTransformationArtifacts:
        logging.info('Entered into data transformation')

        try:
            logging.info('starting data transformation')
            train_df=DataTransformation.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df=DataTransformation.read_data(self.data_validation_artifact.valid_test_file_path)
            
            ## training dataframe
            input_features_train_df=train_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_feature_train_df=train_df[TARGET_COLUMN]
            target_feature_train_df=target_feature_train_df.replace(-1,0)
            #testing dataframe
            input_features_test_df=test_df.drop(columns=[TARGET_COLUMN])
            target_feature_test_df=test_df[TARGET_COLUMN]
            target_feature_test_df=target_feature_test_df.replace(-1,0)

            preprocessor=self.get_data_transformer_object()

            preprocessor_obj=preprocessor.fit(input_features_train_df)
            transformed_input_train_features=preprocessor_obj.transform(input_features_train_df)
            transformed_input_test_features=preprocessor_obj.transform(input_features_test_df)

            train_arr=np.c_[transformed_input_train_features,np.array(target_feature_train_df)]
            test_arr=np.c_[transformed_input_test_features,np.array(target_feature_test_df)]

            save_numpy_array(self.data_transformation_config.transformed_train_data_file_path,train_arr)
            save_numpy_array(self.data_transformation_config.transformed_test_data_file_path,test_arr)
            save_object(self.data_transformation_config.transformed_object_file_path,preprocessor_obj)

            ##Preparing Artifacts
            data_transformation_artifacts=DataTransformationArtifacts(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_data_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_data_file_path
            )

            return data_transformation_artifacts
        except Exception as e:
            raise CustomException(e,sys)

 