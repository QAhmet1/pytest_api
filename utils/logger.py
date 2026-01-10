import logging
import os


def get_logger():
    # Create a custom logger
    logger = logging.getLogger("API_Test_Framework")
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        # Create handlers (Console and File)
        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler('api_tests.log')

        # Create formatters and add it to handlers
        format_str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        c_format = logging.Formatter(format_str)
        f_format = logging.Formatter(format_str)
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        # Add handlers to the logger
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)

    return logger