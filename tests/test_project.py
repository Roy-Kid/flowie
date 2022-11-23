# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-22
# version: 0.0.1

from flowie2 import Project, Task, ParamSpaceIterator, Job
from pathlib import Path
import numpy as np
import shutil

class TestProject:

    def test_launch(self):


        project = Project({'a': [1, 2, 3]}, '.', 'test', 'project for test')
        project.add_exe(Task)
        project.launch()

        tasks = list(project.path.glob('**/Task.pkl'))
        assert tasks
        
        for task in tasks:
            another_task = Task.load(task.parent)
            assert another_task.params == {'a': [1, 2, 3]}

        assert project.path.exists()
        shutil.rmtree(project.path)

    def test_auto_expand_paramspace(self):

        project = Project(
            {'a': ParamSpaceIterator([1, 2, 3]),
             'b': ParamSpaceIterator([4, 5, 6])},
            Path(__file__).parent, 'test', 'project for test')

        project.add_exe(Task)
        project.launch()

        assert len(list(project.path.glob('**/Task.pkl'))) == 3 * 3

        assert project.path.exists()
        shutil.rmtree(project.path)

    def test_file_hierarchy(self):

        project = Project(
            {'project1': 1}, '.', 'test_project'
        )

        class Task1(Task):
            def run(self):
                print('task1')
                self.data['ans'] = 1

        class Task2(Task):
            def run(self):
                print('task1')
                self.data['ans'] = 2

        Job.add_task(Task1)
        Job.add_task(Task2)

        project.add_exe(Job)
        project.launch()

        assert project.path.exists()
        shutil.rmtree(project.path)
