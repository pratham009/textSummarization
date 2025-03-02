from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_1_pipelinedataIngestion import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_2_pipelinedatatransformation import DataTransformationTrainingPipeline
from src.textSummarizer.pipeline.stage_3_pipelinemodeltraining import ModelTrainerPipeline  
from src.textSummarizer.pipeline.stage_4_model_evaluation import ModelEvaluationTrainingPipeline

try:
    STAGE_NAME = "data_ingestion"
    logger.info(f"Initiating {STAGE_NAME} pipeline")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.initiate_data_ingestion()
    logger.info(f"Completed {STAGE_NAME} pipeline")

except Exception as e:
    logger.error(f"Failed to execute {STAGE_NAME} pipeline")
    logger.error(str(e))
logger.info("logger is done")

try: 
    STAGE_NAME = "data_transformation"
    logger.info(f"Initiating {STAGE_NAME} pipeline")
    pipeline = DataTransformationTrainingPipeline()
    pipeline.initiate_data_transformation()
    logger.info(f"Completed {STAGE_NAME} pipeline") 
       
except Exception as e:
    logger.error(f"Failed to execute {STAGE_NAME} pipeline")
    logger.error(str(e))
logger.info("logger is done")


try:
    STAGE_NAME = "model_training"
    logger.info(f"Initiating {STAGE_NAME} pipeline")
    pipeline = ModelTrainerPipeline()
    pipeline.initiate_training()
    logger.info(f"Completed {STAGE_NAME} pipeline")
except Exception as e:  
    logger.error(f"Failed to execute {STAGE_NAME} pipeline")
    logger.error(str(e))
logger.info("logger is done")

STAGE_NAME = "Model Evaluation stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.initiate_model_evaluation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
