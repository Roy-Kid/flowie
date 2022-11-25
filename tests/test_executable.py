# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-21
# version: 0.0.1

import pytest
from flowie.executable import Executable
from flowie.file import delete
from pathlib import Path
import shutil
import pickle


class TestExecutable:
    @pytest.fixture(name="exe", scope="class")
    def init_exe(self):

        path = Path(__file__).parent
        exe = Executable(
            params={"a": 1, "b": [1, 2]},
            name="TestExcutable",
            path=path,
            comment="exe for test",
        )

        yield exe

        delete(exe.path)

    def test_path(self, exe):
        path = Path(__file__).parent
        assert exe.path == Path(f"{path}/{exe.name}.Executable")

    def test_name(self, exe):

        assert exe.name == "TestExcutable"

    def test_create_dir(self, exe):

        exe_dir = Path(exe.path)

        assert exe_dir.exists() and exe_dir.is_dir()

    def test_dump(self, exe):

        exe.serialize()
        expect_exe = Executable.load(exe.path)
        assert expect_exe.comment == "exe for test"
        assert expect_exe.params == {"a": 1, "b": [1, 2]}
