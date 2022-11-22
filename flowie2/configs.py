# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-22
# version: 0.0.1

import logging

class Configs(dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update_log_settings(self['log'])

    @property
    def log_level(self):
        return self['log']['level']
    
    @log_level.setter
    def log_level(self, value):
        self['log']['level'] = value
        self.update_log_settings(self['log'])

    def update_log_settings(self, log_settings:dict):

        logging.basicConfig(level=log_settings['level'])
        

class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

configs = Configs(
    {
        'log': {
            'level': 'DEBUG',
            # 'formatter': CustomFormatter
        }
    }
)
