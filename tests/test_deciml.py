import pytest
from ..deciml.deciml import deciml
from decimal import Decimal

@pytest.mark.parametrize('number, precision, value', [('1.1234467', 4, '1.1234'), ('7.342345', 5, '7.34235'), ('4.3423E-1', 3, '0.434'), ('0.1234567E+2', 3, '12.346')])
def test_deciml_function_valid(number, precision, value):
    assert str(deciml(number, precision)) == str(Decimal(value))

@pytest.mark.parametrize('value', ['dsfsdfs', 'sfd3434dsds', '1000.002.03034'])
def test_decimal_function_nan(value):
    assert str(deciml(value, 10)) == 'NaN'
