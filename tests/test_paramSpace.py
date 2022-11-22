# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-11-22
# version: 0.0.1

import pytest
from flowie2.paramSpace import ParamSpace

class TestParamSpace:

    @pytest.fixture(scope='function', name='ps')
    def init_param_space(self):
        ps = ParamSpace(
            {
                'a': [1, 2, 3],
                'b': [4, 5]
            }
        )

        yield ps

