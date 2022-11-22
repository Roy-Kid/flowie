# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-22
# version: 0.0.1

from .typing import Iterable, Literal, Optional, Any, Callable
import numpy as np
from .dataContainer import DataLike, Data

def reduce(func:Callable, data_set: Iterable[DataLike], field:str, initializer:Optional[Any]):
    data_set = iter(data_set)
    if initializer is None:
        tmp = next(data_set)[field]
    else:
        tmp = initializer

    for data in data_set:
        tmp = func(tmp, data[field])

    return tmp

def reduce_array(data_set: Iterable[DataLike], field:str, op:Literal['mean', 'sum', 'max', 'min']) -> Data:

    tmp = []
    for data in data_set:
        tmp.append(data[field])

    if op == 'mean':
        return np.mean(tmp, axis=0)
    elif op == 'sum':
        return np.sum(tmp, axis=0)
    elif op == 'max':
        return np.max(tmp, axis=0)
    elif op == 'min':
        return np.min(tmp, axis=0)
    else:
        raise ValueError(f'op {op} is not supported')


