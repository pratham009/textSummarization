from src.textSummarizer.logging import logging
from src.textSummarizer.pipeline.stage_1_pipelinedataIngestion import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_2_pipelinedatatransformation import DataTransformationTrainingPipeline


try:
    STAGE_NAME = "data_ingestion"
    logging.info(f"Initiating {STAGE_NAME} pipeline")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.initiate_data_ingestion()
    logging.info(f"Completed {STAGE_NAME} pipeline")

except Exception as e:
    logging.error(f"Failed to execute {STAGE_NAME} pipeline")
    logging.error(str(e))
logging.info("Logging is done")

try: 
    STAGE_NAME = "data_transformation"
    logging.info(f"Initiating {STAGE_NAME} pipeline")
    pipeline = DataTransformationTrainingPipeline()
    pipeline.initiate_data_transformation()
    logging.info(f"Completed {STAGE_NAME} pipeline") 
       
except Exception as e:
    logging.error(f"Failed to execute {STAGE_NAME} pipeline")
    logging.error(str(e))
logging.info("Logging is done")


