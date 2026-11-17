import pytest
from ..deciml.deciml import abs

@pytest.mark.parametrize('value, absolute_value', [(-12.232, '12.232'), (54.342, '54.342'), ('-infinity', 'Infinity')])
def test_abs(value, absolute_value):
    assert str(abs(value)) == absolute_value

@pytest.mark.parametrize('value', ['sadssfs', '123.233.243', 'dsa342ds'])
def test_abs_wrong_input(value):
    assert abs(value) == None