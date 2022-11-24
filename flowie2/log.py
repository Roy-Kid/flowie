# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-22
# version: 0.0.1

import logging
from .configs import configs

log_configs = configs['log']

class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    _format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: grey + _format + reset,
        logging.INFO: grey + _format + reset,
        logging.WARNING: yellow + _format + reset,
        logging.ERROR: red + _format + reset,
        logging.CRITICAL: bold_red + _format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

def get_logger(name: str):

    logger = logging.getLogger(name)
    logger.setLevel(logging._nameToLevel[log_configs['level']])

    # streamHandler = logging.StreamHandler()
    # streamHandler.setFormatter(CustomFormatter())
    # streamHandler.setLevel()
    # logger.addHandler(streamHandler)

    # handler = logging.FileHandler(log_configs['path'])
    return logger