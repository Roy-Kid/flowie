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

configs = Configs(
    {
        'log': {
            'level': 'DEBUG',
        }
    }
)
