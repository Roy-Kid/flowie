# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-21
# version: 0.0.1

import h5py
from .log import get_logger
from pathlib import Path
from .extra.tabulate import tabulate
import glob
import numpy as np
from .typing import PathLike, Union, Dict


class Data(dict):

    log = get_logger("Data")
    # lastModifyTime etc.

    def dump(self, path: PathLike, format: str = "hdf5"):
        write_to = Path(path) / Path("data.hdf5")
        self.log.info(f"dump data to {write_to}")
        with h5py.File(write_to, "a") as f:
            for key, value in self.items():
                try:
                    if key in f:
                        del f[key]
                    f[key] = value
                except TypeError as e:
                    self.log.exception(f"Error when dumping {key} to {path}")
                    raise e

    def __str__(self):
        return tabulate(self, headers=self.keys())

    @classmethod
    def load(cls, path: PathLike, format: str = "hdf5"):

        ins = cls()

        if format == "hdf5":
            read_from = Path(path) / Path("data.hdf5")
            with h5py.File(read_from, "r") as f:
                for key in f.keys():
                    ins[key] = np.array(f[key])

        return ins


DataLike = Union[Data, Dict]


class DataViewer(dict):

    log = get_logger("DataViewer")

    @classmethod
    def load(cls, path: PathLike, format: str = "hdf5"):

        cls_ins = DataViewer._recursive_load(path, format)
        setattr(cls_ins, 'path', Path(path))
        return cls_ins

    @classmethod
    def _recursive_load(cls, path: PathLike, format: str = "hdf5"):
        """
        Recursively load data from path.

        Parameters
        ----------
        path : PathLike
            _description_
        format : str, optional
            _description_, by default 'hdf5'

        Returns
        -------
        DataViewer
            _description_
        """
        path = Path(path)
        cls_ins = cls()
        # We assume that only the final folder contains data.
        if path.is_dir():

            for p in path.iterdir():  # iter dir and file
                dv = cls._recursive_load(p, format)
                cls_ins[p.name] = dv

        else:
            if path.suffix == '.hdf5':
                cls_ins.update(Data.load(path.parent, format))
            else:
                pass

        return cls_ins

    @property
    def ls(self):
        return list(self.keys())

    def cd(self, name):
        return self[name]

    def reload(self):
        self.update(self.load(self.path))

    @property
    def isEmpty(self):
        return bool(len(self))