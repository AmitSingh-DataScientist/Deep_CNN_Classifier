from deepCNNClassifier.config import ConfigurationManager
from deepCNNClassifier.components import Evaluation
from deepCNNClassifier import logger

STAGE_NAME = "Evaluation stage"


def main():
    config = ConfigurationManager()
    val_config = config.get_validation_config()
    evaluation = Evaluation(val_config)
    evaluation.evaluation()
    evaluation.save_score()
    # evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f"**********************************************")
        logger.info(f">>>>>>> stage {STAGE_NAME} is started <<<<<<<<")
        main()
        logger.info(
            f">>>>>>> stage {STAGE_NAME} is completed <<<<<<<<\n\nx============x"
        )
    except Exception as e:
        logger.exception(e)
        raise e
