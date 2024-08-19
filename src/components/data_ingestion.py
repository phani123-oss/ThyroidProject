import sys
import os
import numpy as np
import pandas as pd
from pathlib import Path
from src.constant import *
from src.exception import CustomException
from src.logger import logging

#from src.data_access.thyroid_data import thyroid_data
from src.utils.main_utils import MainUtils
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(artifact_folder, "data_ingestion")
    data_access_dir: str = os.path.join('notebook_implimentation','cleaned_data.csv')  

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_access_dir = self.data_ingestion_config.data_access_dir

    
    def export_data_into_raw_data_dir(self) -> None:
        """
        Method to read data from the data access file and export it to the data ingestion directory.
        """
        try:
            # Creating the target directory if it does not exist
            Path(self.data_ingestion_config.data_ingestion_dir).mkdir(parents=True, exist_ok=True)

            # Read the data from the source CSV file
            df = pd.read_csv(self.data_access_dir)

            # Define the target file path where the data will be saved
            target_file_path = os.path.join(self.data_ingestion_config.data_ingestion_dir, 'cleaned_data.csv')

            # Save the data to the target directory
            df.to_csv(target_file_path, index=False)

            logging.info(f"Data successfully exported from {self.data_access_dir} to {target_file_path}")

        except Exception as e: 
            raise CustomException (e,sys) from e


    def initiate_data_ingestion(self) -> Path:
        """
        Method to initiate the data ingestion process.
        """
        logging.info("Entered initiate_data_ingestion method of DataIngestion class")

        try:
            self.export_data_into_raw_data_dir()

            logging.info("Data successfully ingested")

            logging.info(
                "Exited initiate_data_ingestion method of DataIngestion class"
            )

            return Path(self.data_ingestion_config.data_ingestion_dir)

        except Exception as e: 
            raise CustomException (e,sys) from e