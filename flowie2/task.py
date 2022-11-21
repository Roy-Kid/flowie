# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-21
# version: 0.0.1

from .executable import Executable

class Task(Executable):
    
    def __init__(self, params: dict, path: str, name: str = '', comment: str = '', isSave: bool = True):
        
        super().__init__(params, path, name, comment, isSave)
        
        self.jobs = {}

    def launch(self):
        
        try:
            self._pre()
            self._run()
            self._post()
        except:
            self._on_except()
        finally:
            self._on_finish()

    def _run(self):

        for Job in self.Jobs.values():
            job = Job(self.params, self.path)
            job()

    def add_job(self, job):

        job_id = id(job)
        if job_id not in self.jobs:
            self.jobs[job_id] = job
        else:
            raise KeyError()
