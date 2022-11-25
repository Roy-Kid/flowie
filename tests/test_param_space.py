# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-22
# version: 0.0.1

from flowie.paramSpace import ParamSpace, ParamSpaceIterator
import pytest
import numpy.testing as npt
import numpy as np


class TestParamSpaceIterator:

    def test_list(self):

        actual = [1, 2, 3]
        psi = ParamSpaceIterator(actual)
        assert list(psi) == actual
        for i in psi:
            assert i in actual

    def test_consume(self):

        psi = ParamSpaceIterator([1, 2, 3])
        assert list(psi) == [1, 2, 3]
        assert list(psi) == [1, 2, 3]

    def test_1darray(self):

        actual = np.random.random(5)
        psi = ParamSpaceIterator(actual)
        npt.assert_equal(actual, np.array(list(psi)))

    def test_2darray(self):

        actual = np.random.random((5, 3))
        psi = ParamSpaceIterator(actual)
        for i, p in enumerate(psi):
            npt.assert_equal(actual[i], p)


class TestParamSpace:
    def test_pure_scalar(self):

        ps = ParamSpace({"a": [1, 2, 3], "b": 1})

        assert len(list(ps)) == 1

        for p in ps.expand():
            assert isinstance(p, ParamSpace)

    def test_pure_iter(self):

        ps = ParamSpace(
            {
                "a": ParamSpaceIterator([1, 2, 3]),
                "b": ParamSpaceIterator([4, 5]),
                "c": ParamSpaceIterator([6]),
            }
        )

        assert len(ps) == 2 * 3 * 1

        for p in ps.expand():
            assert isinstance(p, ParamSpace)

    def test_mix_scalar_pure(self):

        ps = ParamSpace({"a": ParamSpaceIterator([1, 2, 3]), "b": [1, 2]})

        assert len(ps) == 3 * 1

        for p in ps.expand():
            assert isinstance(p, ParamSpace)

    def test_guess_name(self):

        with pytest.raises(ValueError):
            ps = ParamSpace({"a": ParamSpaceIterator([1, 2, 3]), "b": [1, 2]})
            assert ps.guess_name()

        ps = ParamSpace({"a": 1, "b": 2})
        assert ps.guess_name() == "a=1_b=2"

        ps = ParamSpace({"a": [1, 2, 3], "b": 1})
        assert ps.guess_name() == "a=[1, 2, 3]_b=1"

        ps = ParamSpace({"a": np.array([1, 2, 3]), "b": 1})
        assert ps.guess_name() == "a=[1 2 3]_b=1"

        ps = ParamSpace({
            "a": ParamSpaceIterator([1, 2, 3]),
            "b": ParamSpaceIterator([4, 5, 6]),            
        })
        for p in ps.expand():
            p.guess_name()