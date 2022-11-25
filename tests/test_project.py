# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-22
# version: 0.0.1

from flowie import Project, Task, ParamSpaceIterator, Job
from flowie.file import delete
from pathlib import Path
import numpy as np
import shutil


class TestProject:
    def test_launch(self):

        project = Project("test", {"a": [1, 2, 3]}, ".", "project for test")
        project.add_exe(Task)
        project.launch()

        tasks = list(project.path.glob("**/Task.pkl"))
        assert tasks

        for task in tasks:
            another_task = Task.load(task.parent)
            assert another_task.params == {"a": [1, 2, 3]}

    def test_auto_expand_paramspace(self):

        project = Project(
            "test",
            {
                "a": ParamSpaceIterator([1, 2, 3]),
                "b": ParamSpaceIterator([4, 5, 6]),
            },
            ".",
            "project for test",
        )

        param_space = project.params
        assert len(param_space.expand()) == 9

        project.add_exe(Task)
        project.launch()

        assert len(list(project.path.glob("**/Task.pkl"))) == 3 * 3

        delete(project.path)

    def test_file_hierarchy(self):

        project = Project("test", {"project1": 1}, ".", "test_project")

        class Task1(Task):
            def run(self):
                print("task1")
                self.data["ans"] = 1

        class Task2(Task):
            def run(self):
                print("task1")
                self.data["ans"] = 2

        Job.add_task(Task1)
        Job.add_task(Task2)

        project.add_exe(Job)
        project.launch()
