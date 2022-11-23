# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-23
# version: 0.0.1

import pytest
from flowie2 import Project, Job

class TestViewer:

    @pytest.fixture(name='test_project', scope='class')
    def init_project(self):

        project = Project(
            {'project1': 1}, '.', 'test_project'
        )

        job_template = Job
        # job_template.add_task()

        project.add_exe(Job)
        