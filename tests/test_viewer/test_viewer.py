# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-23
# version: 0.0.1

import pytest
from flowie2 import Project, Job, Task
import shutil

class TestViewer:

    @pytest.fixture(name='test_project', scope='class')
    def init_project(self):

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
        
        yield project

        assert project.path.exists()
        shutil.rmtree(project.path)

    def test_load_data(self, test_project):

        pass