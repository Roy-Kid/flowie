# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-22
# version: 0.0.1

from .executable import Executable
from .typing import PathLike, List
from .paramSpace import ParamSpace, ParamLike


class Project(Executable):

    params: ParamSpace

    def __init__(
        self,
        name,
        params: ParamLike,
        path: PathLike,
        comment: str = "",
        isSave: bool = True,
    ):
        super().__init__(params, path, name, comment, isSave)

        self.exe:List[type[Executable]] = []

    def add_exe(self, exe):
        if exe not in self.exe:
            self.exe.append(exe)
        else:
            self.log.exception("duplicate adding exe")

    def launch(self):

        params = self.params.expand()
        for param in params:
            for exe in self.exe:
                exe_ins = exe(param, self.path, name=param.guess_name(), isSave=True)
                exe_ins.launch()
