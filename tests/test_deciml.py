import pytest
from ..deciml.deciml import deciml
from decimal import Decimal

@pytest.mark.parametrize('number, precision, value', [('1.1234467', 4, '1.1234'), ('7.342345', 5, '7.34235'), ('4.3423E-1', 3, '0.434'), ('0.1234567E+2', 3, '12.346')])
def test_deciml_function_valid(number, precision, value):
    '''
        Test if the precision is correct
    '''
    assert str(deciml(number, precision)) == str(Decimal(value))

@pytest.mark.parametrize('value', ['dsfsdfs', 'sfd3434dsds', '1000.002.03034'])
def test_decimal_function_none(value):
    '''
        Check if None is returned for not numbers
    '''
    assert deciml(value, 10) == None

@pytest.mark.parametrize('value', ['NaN', 'nan', 'Nan'])
def test_decimal_function_nan(value):
    '''
        Check if 'NaN' is returned for NaN
    '''
    assert str(deciml(value)) == 'NaN'

@pytest.mark.parametrize('value', ['inf', 'infinity', 'Infinity', 'Inf', '+inf', '+Inf', '+infinity', '+Infinity'])
def test_decimal_function_infinity(value):
    '''
        Check if 'Infinity' is returned for infinity
    '''
    assert str(deciml(value)) == 'Infinity'

@pytest.mark.parametrize('value', ['-inf', '-infinity', '-Infinity', '-Inf'])
def test_decimal_function_negative_infinity(value):
    '''
        Check if '-Infinity' is returned for -infinity
    '''
    assert str(deciml(value)) == '-Infinity'

