# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-21
# version: 0.0.1

import h5py
import logging
from pathlib import Path
from .viewer.tabulate import tabulate

class Data(dict):

    log = logging.getLogger('Data')
    # lastModifyTime etc.

    def dump(self, path:str, format:str='hdf5'):
        with h5py.File(Path(path)/Path('data.hdf5') , 'w') as f:
            for key, value in self.items():
                try:
                    f[key] = value
                except TypeError as e:
                    self.log.error(f'Error when dumping {key} to {path}')
                    raise e

    def __str__(self):
        return tabulate(self, headers=self.keys())