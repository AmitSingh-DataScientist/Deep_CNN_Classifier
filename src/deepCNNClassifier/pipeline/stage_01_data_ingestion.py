from deepCNNClassifier.config import ConfigurationManager
from deepCNNClassifier.components import DataIngestion
from deepCNNClassifier import logger 

STAGE_NAME = "Data Ingestion Stage"

def main():
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.unzip_and_clean()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} is started <<<<<<<<")
        main()
        logger.info(f">>>>>>> stage {STAGE_NAME} is completed <<<<<<<<\n\nx============x")
    except Exception as e:
        logger.exception(e)
        raise e