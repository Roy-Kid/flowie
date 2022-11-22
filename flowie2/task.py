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

        self.data = Data()
        self.cache = {}

    def launch(self):
        
        self.log.info(f'Task {self.name} is launched')

        try:
            self.pre()
            self.run()
            self.post()
        except Exception as e:
            self.on_except()
            self.log.error(f'Task {self.name} raise {type(e)}\n msg: {e}')
        finally:
            self.on_finish()
            self.log.info(f'Task {self.name} is finished')

    def __getstate__(self):
        return {k: v for k, v in self.__dict__.items() if k not in ['log', 'cache', 'data', ]}

    def run(self):
        raise NotImplementedError()

    def dump(self):
        super().dump()
        self.data.dump(self.path)

    @classmethod
    def load(cls, path):
        ins = super().load(path)
        ins.data = Data.load(path)
        return ins

