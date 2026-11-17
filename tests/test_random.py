import pytest
from ..deciml.deciml import rint, rdeciml
from typing import cast

@pytest.mark.parametrize('start, end, count', [(1, 100, 5), (45, 53, 3), (350, 460, 10), (120, 320, 1)])
def test_random_integer(start, end, count):
    '''
        Check if random integers are returned within range
    '''
    nums = rint(start, end, count)
    if nums is None:assert False
    elif type(nums) is int:
        assert nums >= start and nums <= end
    else:
        for i in cast(tuple[int,...],nums):
            assert i >= start and i <= end

@pytest.mark.parametrize('start, end, count', [(10, 20, -1), (34, 12, 3), (32, 41, -10)])
def test_random_integer_invalid_arguments(start, end, count):
    '''
        Check if invalid arguments return None
    '''
    if rint(start, end, count) is None:assert True
    else:assert False

@pytest.mark.parametrize('start, end, precision, count', [(1, 100, 4, 5), (45, 53, 5, 3), (350, 460, 7, 10), (34, 12, 3, 5)])
def test_random_number(start, end, precision, count):
    '''
        Check if random numbers are returned within range
    '''
    rdeciml_object = rdeciml(start, end, precision)
    arr = [start, end]
    arr.sort()
    start,end=arr
    for i in rdeciml_object.random(count):
        assert i >= start and i <= end and len(str(i).split('.')[1]) <= precision

@pytest.mark.parametrize('start, end, count, precision', [(10, 20, -1, 4), (32, 41, -10, 2)])
def test_random_number_invalid_arguments(start, end, count, precision):
    '''
        Check if invalid arguments return None
    '''
    rdeciml_object = rdeciml(start, end, precision)
    for i in rdeciml_object.random(count):
        if i is None:assert True
        else:
            print(i)
            assert False

