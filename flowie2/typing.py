# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-22
# version: 0.0.1

from pathlib import Path
from typing import Union, Any, Dict, List, Tuple, Optional, Callable, TypeVar, Generic, Type, cast, overload, TYPE_CHECKING, NewType
import numpy as np

PathLike = Union[str, Path]
number = Union[int, float]
array = NewType('array', np.ndarray)