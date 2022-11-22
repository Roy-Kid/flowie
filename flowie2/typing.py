# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-22
# version: 0.0.1

from pathlib import Path
from typing import *  # noqa
import numpy as np
from .dataContainer import Data
from .paramSpace import ParamSpace

PathLike = Union[str, Path]
Number = Union[int, float]
Array = NewType('Array', np.ndarray)
Data = NewType('Data', Data)
ParamLike = Union[ParamSpace, dict]