import pytest
from ..deciml.deciml import deciml_sort
from typing import cast
from decimal import Decimal

@pytest.mark.parametrize('lis, sorted_list, precision', [(['123.322', '43', '41.123'], ['41.123', '43.0', '123.322'], 3), (['12.32123', '43.3432', '-1.123456'], ['-1.1235', '12.3212', '43.3432'], 4)])
def test_deciml_sort(lis, precision, sorted_list):
    '''
        Check if output is correct
    '''
    if (res:=deciml_sort(lis, precision)) is None:assert False
    print(res)
    if len(cast(list[Decimal],res)) != len(sorted_list):assert False
    for i in range(len(res)):
        if str(res[i]) != sorted_list[i]:assert False
        else:assert True

@pytest.mark.parametrize('lis', [['23.343', 'dssds', '3.43'], ['fdsf3d33d', '23.343.342', '3.432'], ['-23.34', 'fdsf']])
def test_deciml_sort_wrong_input(lis):
    '''
        Check if returns None for wrong arguments
    '''
    if (res:=deciml_sort(lis)) is None:assert True
    else:assert False