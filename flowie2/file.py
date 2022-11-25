# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-23
# version: 0.0.1

from .typing import PathLike
from pathlib import Path
import shutil


def delete(path: PathLike):
    """
    delete a file, or a directory with its content

    Parameters
    ----------
    path : PathLike
        a path to file or directory
    """
    path = Path(path)
    if path.exists():
        shutil.rmtree(path)
