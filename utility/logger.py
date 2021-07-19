import logging

file_log = 'error.log'

logger = logging.getLogger(__name__)

fh = logging.FileHandler(file_log)
fh.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

logger.addHandler(fh)