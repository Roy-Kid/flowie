# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-21
# version: 0.0.1

from .executable import Executable
from pathlib import Path
from .dataContainer import Data

class Task(Executable):
    
    def __init__(self, params: dict, path: str, name: str = '', comment: str = '', isSave: bool = True):
        
        super().__init__(params, path, name, comment, isSave)

        self._data = Data()

    def launch(self):
        
        self.log.info(f'Task {self.name} is launching...')

        try:
            self._pre()
            self._run()
            self._post()
        except:
            self._on_except()
        finally:
            self._on_finish()

    def __getstate__(self):
        return {k: v for k, v in self.__dict__.items() if k != '_data'}

    def _run(self):
        raise NotImplementedError()

    def dump(self):
        super().dump()
        self._data.dump(self.path)

    @classmethod
    def load(cls, path):
        ins = super().load(path)
        ins._data = Data.load(path)
        return ins

