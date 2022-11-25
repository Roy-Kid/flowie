# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-21
# version: 0.0.1

from .executable import Executable
from .typing import List
from .task import Task


class MetaJob(type):
    def __new__(cls, clsname, bases, clsdict):
        clsdict["tasks"] = []  # create tasks when define new Job class
        return super().__new__(cls, clsname, bases, clsdict)


class Job(Executable, metaclass=MetaJob):

    tasks: List[type[Task]]

    def __init__(
        self,
        params: dict,
        path: str,
        name: str = "",
        comment: str = "",
        isSave: bool = True,
    ):
        super().__init__(params, path, name, comment, isSave)

        # An ugly way to share info between Job and its tasks
        self.cache = {}

    def launch(self):

        self.log.info(f"Job {self.name} is launching...")

        try:
            self.pre()
            self.run()
            self.post()
        except Exception as e:
            self.on_except(e)
        finally:
            self.on_finish()

    def run(self):

        for task in self.tasks:
            task = task(self.params, self.path)
            task.recieve_cache(self.cache)
            task.launch()

    @classmethod
    def add_task(cls, task: type[Task]):
        if task not in cls.tasks:
            cls.tasks.append(task)
        else:
            raise KeyError()

        return cls

    @classmethod
    @property
    def n_tasks(cls):
        return len(cls.tasks)
