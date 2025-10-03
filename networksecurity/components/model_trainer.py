from networksecurity.exception.custom_expection import CustomException
from networksecurity.logging.custom_logging import logging
from networksecurity.entity.artifacts_entity import DataTransformationArtifacts,ModelTrainerArtifacts
from networksecurity.entity.config_entity import ModelTrainerConfig
from networksecurity.utils.main_utils.utils import load_numpy_array
from networksecurity.utils.main_utils.utils import get_models_report, save_object, load_object
from networksecurity.utils.ml_utils.metric.classification_metric import get_classification_score
from networksecurity.utils.ml_utils.model.estimator import NetworkModel
import sys, os
import mlflow

class ModelTrainer:
    def __init__(self, data_transformation_artifacts: DataTransformationArtifacts, model_trainer_config: ModelTrainerConfig):
        try:
            self.data_transformation_artifacts=data_transformation_artifacts
            self.model_trainer_config=model_trainer_config
        except Exception as e:
            raise CustomException(e,sys)
    
    def track_ml_flow(self, model, classificationarticfact):
        with mlflow.start_run():
            f1_score=classificationarticfact.f1_score
            precision_score=classificationarticfact.precision_score
            recall_score=classificationarticfact.recall_score

            mlflow.log_metric('f1 score', f1_score)
            mlflow.log_metric('precision', precision_score)
            mlflow.log_metric('recall_score', recall_score)
            mlflow.sklearn.log_model(model,'model')

    def initiate_model_trainer(self)->ModelTrainerArtifacts:
        try:
            train_arr=load_numpy_array(self.data_transformation_artifacts.transformed_train_file_path)
            test_arr=load_numpy_array(self.data_transformation_artifacts.transformed_test_file_path)

            x_train_arr=train_arr[:,:-1]
            y_train_arr=train_arr[:,-1]
            x_test_arr=test_arr[:,:-1]
            y_test_arr=test_arr[:,-1]

            models: dict=self.model_trainer_config.models_to_test
            params: dict=self.model_trainer_config.models_params


            models_report,best_models = get_models_report(x_train_arr,y_train_arr,x_test_arr,y_test_arr, models, params)

            best_accuracy: float= max(models_report.values())

            best_model_name=list(models_report.keys())[list(models_report.values()).index(best_accuracy)]

            best_model=best_models[best_model_name]

            y_train_pred=best_model.predict(x_train_arr)

            train_classification_metric=get_classification_score(y_pred=y_train_pred,y_true=y_train_arr)

            self.track_ml_flow(best_model, train_classification_metric)

            y_test_pred=best_model.predict(x_test_arr)

            test_classification_metric=get_classification_score(y_pred=y_test_pred,y_true=y_test_arr)
            
            self.track_ml_flow(best_model, test_classification_metric)
            ## TRACK MLFLOW

            preprocessor=load_object(self.data_transformation_artifacts.transformed_object_file_path)

            ##Save the model
            model_dir_path=os.path.dirname(self.model_trainer_config.model_path)
            os.makedirs(model_dir_path, exist_ok=True)

            networkSecurity_model=NetworkModel(preprocessor=preprocessor, model=best_model)

            save_object(self.model_trainer_config.model_path, networkSecurity_model)

            return ModelTrainerArtifacts(
                trained_model_path=self.model_trainer_config.model_path,
                trained_metric_artifacts=train_classification_metric,
                test_metric_artifacts=test_classification_metric

            )





        except Exception as e:
            raise CustomException(e,sys)
        

        