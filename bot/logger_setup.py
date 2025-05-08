import logging
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)  # создаст папку, если её нет

def setup_logger(name: str, log_file: str, level=logging.INFO):
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    handler = logging.FileHandler(os.path.join(LOG_DIR, log_file), encoding="utf-8")
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Добавлять хендлер только один раз
    if not logger.handlers:
        logger.addHandler(handler)

    return logger
import logging
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)  # создаст папку, если её нет

def setup_logger(name: str, log_file: str, level=logging.INFO):
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    handler = logging.FileHandler(os.path.join(LOG_DIR, log_file), encoding="utf-8")
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Добавлять хендлер только один раз
    if not logger.handlers:
        logger.addHandler(handler)

    return logger
