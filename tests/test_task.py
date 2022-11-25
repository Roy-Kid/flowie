# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-21
# version: 0.0.1

from flowie.task import Task
from flowie.file import delete
import numpy as np
from pathlib import Path
import shutil


class TestTask:
    def test_dump(self):

        task = Task({"a": 1}, ".", "test", "task for test")
        task.data["b"] = 2
        task.data["c"] = np.random.random((3, 5))
        task.launch()

        another_task = Task.load(task.path)
        assert another_task.params["a"] == 1
        assert another_task.data["b"] == 2
