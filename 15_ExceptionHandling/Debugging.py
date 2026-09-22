import logging


logging.basicConfig(
    level   = logging.DEBUG,
    format  = '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
)

logger = logging.getLogger(__name__)

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')


file_h = logging.FileHandler('app.log')
file_h.setLevel(logging.DEBUG)      # file captures everything
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
file_h.setFormatter(formatter)
logger.addHandler(file_h)

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')