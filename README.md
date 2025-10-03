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
- **Experimentation notebooks:**  
  Includes ready-to-run Jupyter notebooks for prototyping and debugging.

## How to Run

1. **Dependencies**  
   ```
   pip install -r requirements.txt
   ```

2. **Push Data (Optional)**  
   - Configure your MongoDB URL in an `.env` file.
   - Run:
     ```
     python push_data.py
     ```

3. **Run Pipeline**
   ```
   python main.py
   ```

## Configuration

Edit the `data_schema/schema.yaml` for schema requirements and validation rules.

## Contributions

Pull requests and suggestions are welcome! Please check the issues tab for current needs or contact the author for more info.

## Author

- **Rajat Sharma**  
  Email: rajattsharma87077@gmail.com
