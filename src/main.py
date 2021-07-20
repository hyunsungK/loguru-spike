import os

from logger_wrap import initialize


if __name__ == "__main__":
    LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "log")
    logger = initialize(LOG_PATH, file_name="worker.log")
    logger.info("Okay Info")
