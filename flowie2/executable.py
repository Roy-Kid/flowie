# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-21
# version: 0.0.1

import logging, pickle
from pathlib import Path
from .log import get_logger
from .typing import PathLike
from .paramSpace import ParamLike

class Executable:

    def __init__(self, params:ParamLike, path:PathLike, name:str='', comment:str='', isSave:bool=True):
        self.TYPE = str(self.__class__.__name__)
        self.params = params
        self.name = name if name else id(self)
        self.path = Path(path) / Path(f'{self.name}')
        self.comment = comment
        self.log = get_logger(self.TYPE)
        if isSave:
            self.create_dir()

    def create_dir(self):
        self.path.mkdir(parents=True, exist_ok=True)
        self.log.info(f'mkdir {self.path}')

    def dump(self):
        
        with open(self.path / Path(self.TYPE + '.pkl'), 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, path_with_name:Path):
        with open(path_with_name / Path(cls.__name__ + '.pkl'), 'rb') as f:
            return pickle.load(f)

    def launch(self):
        self.log.info(f'launching excutable {self.name}')

    def pre(self):
        self.log.info(f'pre-run excutable {self.name}')

    def post(self):
        self.log.info(f'post-run excutable {self.name}')

    def on_except(self, e):
        self.log.exception(e)

    def on_finish(self):
        self.dump()

    def run(self):
        self.log.info(f'post-run excutable {self.name}')