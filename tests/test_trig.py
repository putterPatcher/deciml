import pytest
from ..deciml.deciml import trig

@pytest.mark.parametrize('input, precision, result', [(0, 5, 0.0), (3.14, 3, 0.001594), (3.432, 4, -0.2863), (1.343, 3, 0.974)])
def test_sin(input, precision, result):
    assert str(trig.sin(input, precision)) == str(result)