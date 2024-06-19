import logging

def logger_init(file_path: str = "log.log"):
    logging.basicConfig(level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S")
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler(file_path)
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    return logger