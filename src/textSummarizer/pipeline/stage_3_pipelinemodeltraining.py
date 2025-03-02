from sympy import im
from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.model_trainer import ModelTrainer    
from src.textSummarizer.logging import logger

class ModelTrainerPipeline:
    def __init__(self):
        pass
    def initiate_training(self):
        try:
            logger.info("Pipeline stage 3: Model Training Initiated")
            config_mgr = ConfigurationManager()
            model_trainer_config = config_mgr.get_model_trainer_config()
            model_trainer = ModelTrainer(model_trainer_config)
            model_trainer.train()
            logger.info("Pipeline stage 3: Model Training Completed")
        except Exception as e:
            logger.error(f"Pipeline stage 3: Model Training Failed: {str(e)}")
            raise Exception(f"Pipeline stage 3: Model Training Failed: {str(e)}")
