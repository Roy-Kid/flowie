# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-24
# version: 0.0.1

from flowie import Project, Task, Job, ParamSpaceIterator
from flowie.dataContainer import Data, DataViewer
from flowie.file import delete
import numpy as np
import numpy.testing as npt
import pytest
import os


class Task1(Task):
    def run(self):
        self.data["ans"] = 1


class Task2(Task):
    def run(self):
        self.data["ans"] = 2


class Task3(Task):
    def run(self):
        self.data["ans"] = 3


class Job1(Job):
    pass


class Job2(Job):
    pass


class TestDataViewer:
    def test_load(self):

        project = Project(
            "test",
            {"a": 1, "b": ParamSpaceIterator([2, 3])},
            ".",
            "test_project",
        )

        Job1.add_task(Task1)
        Job1.add_task(Task2)

        Job2.add_task(Task3)

        project.add_exe(Job1)
        project.add_exe(Job2)

        project.launch()

        dv = DataViewer.load(project.path.absolute())

        assert len(dv) == 2


class TestData:
    def test_load(self):

        task = Task({"a": 1}, ".", "test", "task for test")
        task.data["b"] = 2
        ran_arr = np.random.random((3, 5))
        task.data["c"] = ran_arr
        task.save()

        data = Data.load(task.path.absolute())

        assert data["b"] == 2
        npt.assert_allclose(data["c"], ran_arr)
