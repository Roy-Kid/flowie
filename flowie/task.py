# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-21
# version: 0.0.1

from .executable import Executable
from pathlib import Path
from .dataContainer import Data
from .typing import PathLike


class Task(Executable):
    def __init__(
        self,
        params: dict,
        path: PathLike,
        name: str = "",
        comment: str = "",
        isSave: bool = True,
    ):

        super().__init__(params, path, name, comment, isSave)

        self.data = Data()
        self.cache = {}

    def launch(self):

        self.log.info(f"Task {self.name} is launched")

        try:
            self.pre()
            self.run()
            self.post()
        except Exception as e:
            self.on_except(e)
        finally:
            self.on_finish()

    def __getstate__(self):
        return {
            k: v
            for k, v in self.__dict__.items()
            if k
            not in [
                "log",
                "cache",
                "data",
            ]
        }

    @classmethod
    def load(cls, path):
        ins = super().load(path)
        ins.data = Data.load(path)
        return ins

    def on_finish(self):
        self.save()

    def save(self):
        super().save()
        self.data.dump(self.path)

    def recieve_cache(self, cache):

        self.cache.update(cache)
