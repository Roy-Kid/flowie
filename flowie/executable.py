# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-21
# version: 0.0.1

import pickle
from pathlib import Path
from .log import get_logger
from .typing import PathLike
from .paramSpace import ParamLike, ParamSpace


class Executable:
    def __init__(
        self,
        params: ParamLike,
        path: PathLike,
        name: str = "",
        comment: str = "",
        isSave: bool = True,
    ):
        self.TYPE = str(self.__class__.__name__)
        self.params = ParamSpace(params)
        self.name = name if name else self.params.guess_name()
        self.path = Path(path) / Path(f"{self.name}.{self.TYPE}")
        self.comment = comment
        self.log = get_logger(self.TYPE)
        self.isSave = isSave
        if isSave:
            self.mkdir()

    def mkdir(self):
        self.path.mkdir(parents=True, exist_ok=True)
        self.log.info(f"mkdir {self.path}")

    def serialize(self):

        with open(self.path / Path(self.TYPE + ".pkl"), "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, path_with_name: Path):
        with open(path_with_name / Path(cls.__name__ + ".pkl"), "rb") as f:
            return pickle.load(f)

    def save(self):
        if self.isSave and self.path.exists():
            self.serialize()

    def launch(self):
        self.log.info(f"launching excutable {self.name}")

    def pre(self):
        self.log.info(f"pre-run excutable {self.name}")

    def post(self):
        self.log.info(f"post-run excutable {self.name}")

    def on_except(self, e):
        self.log.exception(e)

    def on_finish(self):
        self.log.info(f"finish excutable {self.name}")

    def run(self):
        self.log.info(f"post-run excutable {self.name}")
