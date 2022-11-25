# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-22
# version: 0.0.1

import logging


class Configs(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
