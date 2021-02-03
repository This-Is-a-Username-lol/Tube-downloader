# logger.py - provides a helpful function to generate a new custom named logger
import logging

# application wide configuration
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

def get_logger(logger_name):
    return logging.get_logger(logger_name)
