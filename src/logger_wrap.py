import os
import sys

from loguru import logger


def initialize(log_path, file_name):
    logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
    logger.add(os.path.join(log_path, file_name), rotation="500 MB")
    return logger


