import logging
import os
from config import LOG_LEVEL

def get_logger(name: str) -> logging.Logger:

    # Converting numeric level logger
    numeric_level = getattr(logging, LOG_LEVEL, logging.INFO)

    # Logger configuration
    logger = logging.getLogger(name)
    logger.setLevel(numeric_level)

    # Handler to STDOUT
    ch = logging.StreamHandler()
    ch.setLevel(numeric_level)

    # Log format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    # Add the handler
    logger.addHandler(ch)

    return logger
