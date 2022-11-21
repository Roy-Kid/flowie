# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-21
# version: 0.0.1

import logging, pickle
from pathlib import Path

class Executable:

    def __init__(self, params:dict, path:str, name:str='', comment:str='', isSave:bool=True):
        self.TYPE = self.__class__.__name__
        self.params = params
        self.name = name if name else id(self)
        self.path = Path(path) / Path(f'{self.TYPE}_{self.name}')
        self.comment = comment
        self.log = logging.getLogger(self.TYPE)
        if isSave:
            self.create_dir()

    def create_dir(self):

        self.path.mkdir(parents=True, exist_ok=True)

    def dump(self):
        
        with open(self.path / Path(self.TYPE + '.pkl'), 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, path:Path):
        with open(path / Path(cls.__name__ + '.pkl'), 'rb') as f:
            return pickle.load(f)

    def launch(self):
        pass

    def _pre(self):
        pass

    def _post(self):
        pass

    def _on_except(self):
        pass

    def _on_finish(self):
        pass