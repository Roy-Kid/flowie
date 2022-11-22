# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-22
# version: 0.0.1

from .typing import Iterable, List, Union, Dict

class ParamSpaceIterator:

    def __init__(self, Iterable:Iterable):
        self.iterable = iter(Iterable)

    def __iter__(self):
        return self.iterable
    
    def __next__(self):
        return next(self.iterable)

class ParamSpace(dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __iter__(self):

        return iter(self.expand())
    
    def expand(self)->List:

        iters = {}
        scalars = {}
        # extract iterators
        for k, v in self.items():
            if isinstance(v, ParamSpaceIterator):
                iters[k] = v
            else:
                scalars[k] = v

        if not len(iters):
            return [scalars]

        # get all combinations
        def _expand(iters):
            if len(iters) == 1:
                k, v = list(iters.items())[0]
                return [{k: vv} for vv in v]
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
    
ParamLike = Union[Dict, ParamSpace]