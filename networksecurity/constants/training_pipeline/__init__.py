"""
Constants variables for training
"""

TARGET_COLUMN: str = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str = "Artifacts"
RAWDATA_FILE_NAME: str = "raw.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"


"""
Data ingestion related constants starts with DATA_INGESTION VAR NAME
"""

DATA_INGESTION_DATABASE_NAME: str = "NETWORKSECURITY"
DATA_INGESTION_COLLECITON_NAME: str = "NETWORKSECURITYDATA"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2
