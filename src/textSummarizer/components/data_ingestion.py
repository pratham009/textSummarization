import os
import zipfile
import urllib.request as request  # Fix import for urlretrieve
from src.textSummarizer.logging import logger
from src.textSummarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_file(self):  # Fixed method name
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"File downloaded at {filename}")

            # Check if file is a valid ZIP
            if not zipfile.is_zipfile(filename):
                logger.error("Downloaded file is not a valid ZIP file.")
                raise ValueError("Downloaded file is not a ZIP file")
        else:
            logger.info(f"File already exists at {self.config.local_data_file}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        if not zipfile.is_zipfile(self.config.local_data_file):
            logger.error("Downloaded file is not a valid ZIP file.")
            raise ValueError("Downloaded file is not a ZIP file")

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"Extracted zip file to {unzip_path}")
