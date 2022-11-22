# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-22
# version: 0.0.1

from .executable import Executable
from .typing import ParamLike, PathLike
from .paramSpace import ParamSpace

class Project(Executable):

    params: ParamSpace

    def __init__(self, params: ParamLike, path: PathLike, name: str = '', comment: str = '', isSave: bool = True):
        super().__init__(ParamSpace(params), path, name, comment, isSave)

        self.exe = {}

    def add_exe(self, exe):
        exe_id = id(exe)
        if exe_id not in self.exe:
            self.exe[exe_id] = exe
        else:
            self.log.exception('duplicate adding exe')
        
    def launch(self):
        
        params = self.params.expand()
        for param in params:
            for exe in self.exe.values():
                exe_ins = exe(param, self.path, isSave=True)
                exe_ins.launch()