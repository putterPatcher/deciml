import pytest
from ..deciml.deciml import rint, rdeciml

@pytest.mark.parametrize('start, end, count', [(1, 100, 5), (45, 53, 3), (350, 460, 10)])
def test_random_integer(start, end, count):
    for i in rint(start, end, count):
        assert i >= start and i <= end

@pytest.mark.parametrize('start, end, precision, count', [(1, 100, 4, 5), (45, 53, 5, 3), (350, 460, 7, 10)])
def test_random_number(start, end, precision, count):
    rdeciml_object = rdeciml(start, end, precision)
    for i in rdeciml_object.random(count):
        assert i >= start and i <= end and len(str(i).split('.')[1]) <= precision
