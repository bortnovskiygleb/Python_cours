import logging
from bot_config import time


def logg_this(message_to_log):
    logging.basicConfig(filename='logs/log ' + ''.join(str(time).split(':')) + '.log', level=logging.INFO, filemode='w')
    logging.info(message_to_log)
