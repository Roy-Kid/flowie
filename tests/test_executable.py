# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-21
# version: 0.0.1

import pytest
from flowie2.executable import Executable
from pathlib import Path
import shutil
import pickle

class TestExecutable:

    @pytest.fixture(name='exe', scope='class')
    def init_exe(self):
        
        path = Path(__file__).parent
        exe = Executable(
            params={'a': 1, 'b': [1, 2]}, 
            name='test',
            path=path,
            comment='exe for test')

        yield exe

    def test_name(self, exe):

        assert exe.name == 'testexe'
        exe1 = Executable(params={}, path='')
        assert exe1.name == id(exe1)

    def test_create_dir(self, exe):

        exe_dir = Path(exe.path)

        assert exe_dir.exists() and exe_dir.is_dir()
        
    def test_dump(self, exe):

        exe.dump()
        with open(Path(exe.path)/'Executable.pkl', 'rb') as f:
            exe = pickle.load(f)
            assert exe.comment == 'exe for test'
            assert exe.params == {'a': 1, 'b': [1, 2]}
    

