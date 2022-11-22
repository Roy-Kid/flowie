# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-22
# version: 0.0.1

from .executable import Executable

class Project(Executable):

    def __init__(self, params: dict, path: str, name: str = '', comment: str = '', isSave: bool = True):
        super().__init__(params, path, name, comment, isSave)

        self.exe = {}

    def add_exe(self, exe):
        exe_id = id(exe)
        if exe_id not in self.exe:
            self.exe[exe_id] = exe
        else:
            raise KeyError()
        
    def launch(self):
        pass