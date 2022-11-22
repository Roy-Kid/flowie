# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-22
# version: 0.0.1

from flowie2.project import Project
from flowie2.task import Task
from pathlib import Path
import numpy as np

class TestProject:

    def test_launch(self):


        project = Project({'a': [1, 2, 3]}, Path(__file__).parent, 'test', 'project for test')
        project.add_exe(Task)
        project.launch()

        for task in project.path.glob('**/*.task'):
            another_task = Task.load(task)
            assert another_task.params == {'a': [1, 2, 3]}

        for task in project.path.glob('**/*.task'):
            task.unlink()
        project.path.rmdir()