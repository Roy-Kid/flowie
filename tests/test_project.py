# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-22
# version: 0.0.1

from flowie2.project import Project
from flowie2.task import Task
from flowie2.paramSpace import ParamSpaceIterator
from pathlib import Path
import numpy as np
import shutil

class TestProject:

    def test_launch(self):


        project = Project({'a': [1, 2, 3]}, Path(__file__).parent, 'test', 'project for test')
        project.add_exe(Task)
        project.launch()

        tasks = list(project.path.glob('**/Task.pkl'))
        assert tasks
        
        for task in tasks:
            another_task = Task.load(task.parent)
            assert another_task.params == {'a': [1, 2, 3]}

        shutil.rmtree(project.path)

    def test_auto_expand_paramspace(self):

        project = Project(
            {'a': ParamSpaceIterator([1, 2, 3]),
             'b': ParamSpaceIterator([4, 5, 6])},
            Path(__file__).parent, 'test', 'project for test')

        project.add_exe(Task)
        project.launch()

        assert len(list(project.path.glob('**/Task.pkl'))) == 3 * 3

        shutil.rmtree(project.path)