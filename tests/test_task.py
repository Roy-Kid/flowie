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
        task._data['b'] = 2
        task._data['c'] = np.random.random((3, 5))
        task.dump()

        