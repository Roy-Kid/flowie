# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-22
# version: 0.0.1

from pathlib import Path
from typing import Union, NewType, Optional, List, Dict, Iterable
import numpy as np


PathLike = Union[str, Path]
Number = Union[int, float]
Array = NewType("Array", np.ndarray)
