# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-23
# version: 0.0.1

from flowie2 import Job, Task
import pytest

class TestJob:

    def test_add_task(self):

        class Job1(Job):
            pass

        assert Job1.tasks == []
        Job1.add_task(Task)
        assert Job1.n_tasks == 1

        with pytest.raises(KeyError):
            Job1.add_task(Task)

    