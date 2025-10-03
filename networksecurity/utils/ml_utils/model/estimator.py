from networksecurity.exception.custom_expection import CustomException
import sys

class NetworkModel:
    def __init__(self, model:object, preprocessor: object):
        try:
            self.preprocessor=preprocessor
            self.model=model
        except Exception as e:
            raise CustomException(e,sys)

    def predict(self, X):
        try:
            preprocessed_X=self.preprocessor.transform(X)
            y_pred=self.model.predict(preprocessed_X)
            return y_pred
        except Exception as e:
            raise CustomException(e,sys)
