# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-22
# version: 0.0.1

def linear(start, end, step):
    return [start + i * step for i in range(int((end - start) / step) + 1)]

class ParamSpace(dict):

    def __init__(self, *args, **kwargs):
        super(ParamSpace, self).__init__(*args, **kwargs)

    # def __iter__(self):
    #     return ParamSpaceIterator(self)
    
