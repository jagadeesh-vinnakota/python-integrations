import logging

# logs all the logs which are above DEBUG level of severity with date and message format
logging.basicConfig(format='%(asctime)s - %(message)s', level='DEBUG')

person = 'jagadeesh'
logging.info(f'{person}, This log is indicates INFO')
logging.debug(f'{person}, This log indicates DEBUG')
logging.error(f'{person}, This log indicates ERROR')
logging.critical(f'{person}, This log indicates CRITICAL')
logging.warning(f'{person}, This log indicates WARNING')

