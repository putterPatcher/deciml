import pytest
from ..deciml.deciml import algbra

@pytest.mark.parametrize('values, precision, result', [(['12.1234', 5.4321, 3.043], 3, '20.599'), ([3.453213, '4.234321'], 4, '7.6875'), ([12.323, -34.343, 4.564], 2, '-17.46')])
def test_addition(values, precision, result):
    '''
        Check if result is correct
    '''
    assert str(algbra.add(*values, pr=precision)) == result

@pytest.mark.parametrize('values', [['dsadsa', '23.2343' ], ['23343.3432.2324', '343.434'], ['sads3432fsd', 13.2323], 'dsads', '3434.4343.434', 'dsd324sdfs'])
def test_addition_error(values):
    '''
        Check if wrong arguments return None
    '''
    assert algbra.add(values) == None

@pytest.mark.parametrize('values, precision, result', [(['12.234543', '43.3453'], 3, '-31.111'), (['23.2321', '-4.34543', '1.23432'], 4, '26.3432')])
def test_substraction(values, precision, result):
    '''
        Check if result is correct
    '''
    assert str(algbra.sub(*values, pr=precision)) == result

@pytest.mark.parametrize('values', [['dsadsa', '23.2343' ], ['23343.3432.2324', '343.434'], ['sads3432fsd', 13.2323], 'dsads', '3434.4343.434', 'dsd324sdfs'])
def test_substraction_error(values):
    '''
        Check if wrong arguments return None
    '''
    assert algbra.sub(*values) == None

@pytest.mark.parametrize('values, precision, result', [(['12.234543', '43.3453'], 3, '530.31'), (['23.2321', '-4.34543', '1.23432'], 4, '-124.6089')])
def test_multiplication(values, precision, result):
    '''
        Check if result is correct
    '''
    assert str(algbra.mul(*values, pr=precision)) == result

@pytest.mark.parametrize('values', [['dsadsa', '23.2343' ], ['23343.3432.2324', '343.434'], ['sads3432fsd', 13.2323], 'dsads', '3434.4343.434', 'dsd324sdfs'])
def test_multiplication_error(values):
    '''
        Check if wrong arguments return None
    '''
    assert algbra.mul(*values) == None

@pytest.mark.parametrize('values, precision, result', [([12.34543, 65.34564], 4, '0.1889'), (['65.4543', -4.4532], 3, '-14.698')])
def test_division(values, precision, result):
    '''
        Check if result is correct
    '''
    assert str(algbra.div(values[0], values[1], precision)) == result

@pytest.mark.parametrize('values', [['dsadsa', '23.2343' ], ['23343.3432.2324', '343.434'], ['sads3432fsd', 13.2323]])
def test_division_error(values):
    '''
        Check if wrong arguments return None
    '''
    assert algbra.div(*values) == None

@pytest.mark.parametrize('value', ['dsads', '3434.4343.434', 'dsd324sdfs'])
def test_division_type_error(value):
    '''
        Check type error
    '''
    with pytest.raises(TypeError):
        assert algbra.div(value)

def test_division_zero():
    '''
        Check if None for zero as denominator
    '''
    assert algbra.div(12.343, 0) == None

@pytest.mark.parametrize('base, exponent, precision, result', [('12.343', '3.4322', 4, '5571.5268'), (12.343, -3.45, 3, '0.0001716'), (12.1232, 0, 5, '1'), (0, 2.3433, 2, '0'), (2, 3, 0, '8'), (2, 3, 3, '8.0')])
def test_exponentiation(base, exponent, precision, result):
    '''
        Check if result is correct
    '''
    assert str(algbra.pwr(base, exponent, precision)) == result

@pytest.mark.parametrize('base, exponent', [(-12.343, 2.343), (-34.3223, 3.4533), ['dsadsa', '23.2343' ], ['23343.3432.2324', '343.434'], ['sads3432fsd', 13.2323]])
def test_exponentiation_error(base, exponent):
    '''
        Check if wrong arguments return None
    '''
    assert algbra.pwr(base, exponent) == None

@pytest.mark.parametrize('value', ['dsads', '3434.4343.434', 'dsd324sdfs'])
def test_exponentiation_type_error(value):
    '''
        Check type error
    '''
    with pytest.raises(TypeError):
        assert algbra.pwr(value)

@pytest.mark.parametrize('number, precision, result', [(12.32123, 4, '1.0907'), (3.4343, 3, '0.536')])
def test_logarithm(number, precision, result):
    '''
        Check if result is correct
    '''
    assert str(algbra.log(number, pr=precision)) == result

@pytest.mark.parametrize('number, base, precision, result', [(12.2345, 4, 3, '1.806'), (12, '23.56432', 5, '0.78643')])
def test_logarithm_with_base(number, base, precision, result):
    '''
        Check if result is correct
    '''
    assert str(algbra.log(number, base, precision)) == result

@pytest.mark.parametrize('number, base', [(-12.343, 2.343), (-34.3223, 3.4533), ['dsadsa', '23.2343' ], ['23343.3432.2324', '343.434'], ['sads3432fsd', 13.2323]])
def test_logarithm_error(number, base):
    '''
        Check if wrong arguments return None
    '''
    assert algbra.log(number, base) == None
