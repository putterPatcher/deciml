import pytest
from ..deciml.deciml import trig

@pytest.mark.parametrize('input, precision, result', [(0, 5, 0.0), (3.14, 3, 0.001594), (3.432, 4, -0.2863), (1.343, 3, 0.974), (7.3533, 3, 0.877)])
def test_sin(input, precision, result):
    assert str(trig.sin(input, precision)) == str(result)

@pytest.mark.parametrize('input', ['dsads', 'dasd3234dsd', '234.3434.4343'])
def test_sin_error(input):
    assert trig.sin(input) == None

@pytest.mark.parametrize('input, precision, result', [(0, 5, 1.0), (3.14, 3, -1.0), (3.432, 4, -0.9581), (1.343, 3, 0.226), (7.3533, 3, '0.480')])
def test_cos(input, precision, result):
    assert str(trig.cos(input, precision)) == str(result)

@pytest.mark.parametrize('input', ['dsads', 'dasd3234dsd', '234.3434.4343'])
def test_cos_error(input):
    assert trig.cos(input) == None

@pytest.mark.parametrize('input, precision, result', [(0, 5, 0.0), (3.14, 3, -0.001593), (3.432, 4, 0.2989), (1.343, 3, 4.314), (7.3533, 3, 1.828)])
def test_tan(input, precision, result):
    assert str(trig.tan(input, precision)) == str(result)

@pytest.mark.parametrize('input', ['dsads', 'dasd3234dsd', '234.3434.4343'])
def test_tan_error(input):
    assert trig.tan(input) == None
