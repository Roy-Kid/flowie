# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-21
# version: 0.0.1

from .executable import Executable


class Job(Executable):

    def __init__(self, params: dict, path: str, name: str = '', comment: str = '', isSave: bool = True):
        super().__init__(params, path, name, comment, isSave)

        self.tasks = {}

    def launch(self):
        
        self.log.info(f'Job {self.name} is launching...')

        try:
            self._pre()
            self._run()
            self._post()
        except:
            self._on_except()
        finally:
            self._on_finish()

    def run(self):

        for task in self.tasks.values():
            task = task(self.params, self.path)
            task()



    def add_task(self, task):

        task_id = id(task)
        if task_id not in self.tasks:
            self.tasks[task_id] = task
        else:
            self.log.error(f'{task} duplicate adding')
            raise KeyError()