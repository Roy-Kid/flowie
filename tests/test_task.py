# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-21
# version: 0.0.1

from flowie2.task import Task
import numpy as np
from pathlib import Path

class TestTask:

    def test_dump(self):

        task = Task({'a': 1}, Path(__file__).parent, 'test', 'task for test')
        task.data['b'] = 2
        task.data['c'] = np.random.random((3, 5))
        task.dump()

        another_task = Task.load(task.path)
        assert another_task.params['a'] == 1
        assert another_task.data['b'] == 2
        