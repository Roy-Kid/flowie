# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-21
# version: 0.0.1

import h5py
import logging
from pathlib import Path
from .viewer.tabulate import tabulate
import glob
import numpy as np

class Data(dict):

    log = logging.getLogger('Data')
    # lastModifyTime etc.

    def dump(self, path:str, format:str='hdf5'):
        write_to = Path(path)/Path('data.hdf5')
        self.log.info(f'dump data to {write_to}')
        with h5py.File(write_to, 'w') as f:
            for key, value in self.items():
                try:
                    f[key] = value
                except TypeError as e:
                    self.log.error(f'Error when dumping {key} to {path}')
                    raise e

    def __str__(self):
        return tabulate(self, headers=self.keys())

    @classmethod
    def load(cls, path):

        ins = cls()

        path = Path(path)
        if path.is_dir():
            hdf5_list = glob.glob('*.hdf5', root_dir=path)

            if not len(hdf5_list):
                msg = f'no hdf5 file found, or {path} is not a job path'
                ins.log.error(msg)
                raise FileNotFoundError(msg)
            for hf in hdf5_list:

                with h5py.File(path/Path(hf)) as f:
                    for key, value in f.items():
                        ins[key] = np.array(value)
            return ins
        elif path.is_file():

                with h5py.File(path/Path(hf)) as f:
                    for key, value in f.items():
                        ins[key] = np.array(value)

        return ins  
