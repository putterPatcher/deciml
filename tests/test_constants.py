import pytest
from ..deciml.deciml import constant

@pytest.mark.parametrize('precision, pi_value, e_value', [(4, '3.1415', '2.7182'), (7, '3.1415926', '2.7182818'), (10, '3.1415926535', '2.7182818284')])
def test_pi_and_e_value(precision, pi_value, e_value):
    assert str(constant.pi(precision)) == str(pi_value)
    assert str(constant.e(precision)) == str(e_value)
