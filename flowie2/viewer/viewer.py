# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-23
# version: 0.0.1

from ..typing import PathLike
from ..log import get_logger
from ..dataContainer import Data

class Viewer:

    def __init__(self, path: PathLike):

        self.load(path)
        self.log = get_logger('Viewer')
        self.data_tree = {}

    def load(self, path):

        if not path.exists():
            self.log.exception(f'{path} not found')

        self._recursive_load(path)

    def _recursive_load(self, path):

        if path.is_dir():
            for p in path.iterdir():
                self._recursive_load(p)
        else:
            data = Data.load(path)
            self.data_tree[path] = data

    
    