import os
from src.logger_wrap import initialize


def test_initialize_logger():
    LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "log")
    result_logger = initialize(LOG_PATH, 'test.log')

    assert result_logger is not None
