# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-22
# version: 0.0.1

from .typing import Iterable, List, Union, Dict
from copy import deepcopy


class ParamSpaceIterator:
    def __init__(self, Iterable: Iterable):
        self.iterable = Iterable

    def __iter__(self):
        return iter(self.iterable)

    def __next__(self):
        return next(self)
    
    def __repr__(self):
        return f'<flowie.ParamSpaceIterator {" ".join(self.iterable)}>'


class ParamSpace(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __iter__(self):

        return iter(self.expand())

    def expand(self) -> List['ParamSpace']:

        iters = {}
        scalars = {}
        # extract iterators
        for k, v in self.items():
            if isinstance(v, ParamSpaceIterator):
                iters[k] = deepcopy(v)
            else:
                scalars[k] = v

        if not len(iters):
            return [ParamSpace(scalars)]

        # get all combinations
        def _expand(iters):
            if len(iters) == 1:
                return [ParamSpace(k=vv) for k,v in iters.items() for vv in v]
            else:
                tmp = []
                k, v = iters.popitem()
                sub = _expand(iters)
                for vv in v:
                    for s in sub:
                        ps = ParamSpace(s)
                        ps[k] = vv
                        tmp.append(ps)

                return tmp

        tmp = _expand(iters)

        for t in tmp:
            t.update(scalars)

        return tmp

    def __len__(self):
        return len(self.expand())

    def guess_name(self):
        """
        guess the name of this param space. This method should be called in a SIMPLE paramSpace, which do not contain any paramSpaceIterator.

        Returns
        -------
        str
            a name reasoned from this param space
        """
        tmp = {}
        for k, v in self.items():
            # v can not be ParamSpaceIterator
            if isinstance(v, ParamSpaceIterator):
                raise ValueError(
                    "Can not guess name from a paramSpace which contains ParamSpaceIterator"
                )
            try:
                str_k = str(k)
                str_V = str(v)
            except:
                raise ValueError(
                    f"Can not guess name from a paramSpace which contains non-str key or value, which is {k} and {v}"
                )

            tmp[str_k] = str_V

        return "_".join([f"{k}={v}" for k, v in tmp.items()])


ParamLike = Union[Dict, ParamSpace]
