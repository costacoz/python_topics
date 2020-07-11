import logging

"""
    This section logs into the sys.stderr:
"""

logging.debug('This is debug logging message')
logging.error('This is error logging message')
logging.info('This is info logging message')
logging.warning('This is warning logging message')
logging.critical('This is critical logging message')
logging.warning('Statistics \'%s\' file not found!', 'stats.data')

"""
    This section logs into the file:
"""

logger = logging.getLogger('myapp')
handler = logging.FileHandler('output_messages.log')
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)


logger.info('Hello there, this is INFO..')
logger.critical('Hello there, this is INFO..')
logger.warning('This is WARNING message!')