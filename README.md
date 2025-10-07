

# NetworkSecurity
**NetworkSecurity** is a modular Python-based project focused on network security data ingestion, validation, transformation, and model training, with a strong focus on phishing detection.
## Project Structure
- **Network_Data/**: Contains `phisingData.csv`, the main dataset used for analysis.
- **data_schema/**: Contains `schema.yaml` for data validation configurations.
- **networksecurity/**
  Source code structured in submodules for:
  - Data Ingestion
  - Data Validation
  - Data Transformation
  - Model Training
  - Exception handling and Logging
  - Pipeline utilities
- **notebooks/**
  Jupyter notebooks for development, experimentation, and schema/method prototyping.
- **main.py**
  Entrypoint script for running the pipeline end-to-end (data ingestion, validation, transformation, trainer).
- **push_data.py**
  Utility to convert CSV data and push it to MongoDB.
- **requirements.txt**
  Python dependencies for the project: pandas, numpy, pymongo, certifi, scikit-learn, pyyaml, dill, mlflow, python-dotenv.
- **setup.py**
  Packaging script for easy installation.
- **Dockerfile**
  (Pending content) For containerizing the pipeline.
## Features
- **End-to-end data pipeline:**
  Ingests network phishing data and processes it for machine learning.
- **Modular components:**
  Code is organized for scalability and maintainability.
- **MongoDB integration:**
  Easily push raw data to a NoSQL database for scalable storage.
- **YAML schema validation:**
  Customizable data validation via `schema.yaml`.
