import logging


formatter = logging.Formatter('%(asctime)s %(levelname)s [%(name)s::%(funcName)s(%(thread)d)] %(message)s')

logger = logging.getLogger('Whole')
logger.setLevel(logging.INFO)

file_logger = logging.FileHandler(filename='whole.log')
file_logger.setFormatter(formatter)

logger.addHandler(file_logger)