# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-23
# version: 0.0.1

import pytest
from flowie2 import Project, Job, Task
import shutil

class TestViewer:

    def test_load(self):
        
        project = Project(
            {'project1': 1}, '.', 'test_project'
        )

        class Task1(Task):
            def run(self):
                print('task1')
                self.data['ans'] = 1

        class Task2(Task):
            def run(self):
                print('task2')
                self.data['ans'] = 2

        class Task3(Task):
            def run(self):
                print('task3')
                self.data['ans'] = 3

        class Job1(Job):
            pass

        class Job2(Job):
            pass

        Job1.add_task(Task1)
        Job1.add_task(Task2)

        Job2.add_task(Task3)

        project.add_exe(Job1)
        project.add_exe(Job2)
        
        # yield project