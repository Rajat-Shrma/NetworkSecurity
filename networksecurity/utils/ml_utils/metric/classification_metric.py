from networksecurity.entity.artifacts_entity import ClassificationMetricArtifacts
from networksecurity.exception.custom_expection import CustomException
from sklearn.metrics import(
    f1_score,
    precision_score,
    recall_score
)

import sys

def get_classification_score(y_true, y_pred)->ClassificationMetricArtifacts:
    try:
        model_f1_score=f1_score(y_true,y_pred)
        model_precision_score=precision_score(y_pred=y_pred,y_true=y_true)
        model_recall_score=recall_score(y_pred=y_pred,y_true=y_true)

        classification_metric=ClassificationMetricArtifacts(
            f1_score=model_f1_score,
            precision_score=model_precision_score,
            recall_score=model_recall_score
        )

        return classification_metric
    except Exception as e:

        raise CustomException(e,sys)