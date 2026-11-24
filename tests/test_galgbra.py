import pytest
from ..deciml.deciml import galgbra
from typing import cast

def test_add():
    result = galgbra.add([12.33542, 23.267632, 'dsfsfs'], [23.25443, 34.3, '4.343'], ['43.3453', 6.343222, '34'], pr=3)
    expected = [78.935, 63.911, None]
    print(result, "?????")
    if result:
        for r, e in zip(result, expected):
            assert str(r) == str(e)
    else:assert False

def test_add_none():
    result = cast(tuple[None],galgbra.add(['sdad'], [12.3332]))
    assert len(result) == 1
    assert result[0] == None

@pytest.mark.parametrize('arg', ['sdsfs', '34325.3424.2433', 'fsf3242sdfs'])
def test_add_wrong_argument(arg):
    assert galgbra.add(arg) == None

def test_sub():
    result = galgbra.sub([12.33542, 23.267632, 'dsfsfs'], [23.25443, 34.3, '4.343'], ['43.3453', 6.343222, '34'], pr=3)
    expected = [-54.264, -17.376, None]
    if result:
        for r, e in zip(result, expected):
            assert str(r) == str(e)
    else:assert False

def test_sub_none():
    result = cast(tuple[None],galgbra.sub(['sdad'], [12.3332]))
    assert len(result) == 1
    assert result[0] == None

@pytest.mark.parametrize('arg', ['sdsfs', '34325.3424.2433', 'fsf3242sdfs'])
def test_sub_wrong_argument(arg):
    assert galgbra.sub(arg) == None

def test_mul():
    result = galgbra.mul([12.33542, 23.267632, 'dsfsfs'], [23.25443, 34.3, '4.343'], ['43.3453', -6.343222, '34'], pr=3)
    expected = [12433.736, -5062.397, None]
    if result:
        for r, e in zip(result, expected):
            assert str(r) == str(e)
    else:assert False

def test_mul_none():
    result = cast(tuple[None],galgbra.mul(['sdad'], [12.3332]))
    assert len(result) == 1
    assert result[0] == None

@pytest.mark.parametrize('arg', ['sdsfs', '34325.3424.2433', 'fsf3242sdfs'])
def test_mul_wrong_argument(arg):
    assert galgbra.mul(arg) == None

def test_div():
    result = galgbra.div([12.2343, 45.34432, 0.4343, 45], [3.454332, '87.54332', -0.0324, 'fsdfs'], 3)
    expected = [3.542, 0.518, -13.404, None]
    if result:
        for r, e in zip(result, expected):
            assert str(r) == str(e)
    else:assert False

def test_div_none():
    result = cast(tuple[None],galgbra.div(['sdad'], [12.3332]))
    assert len(result) == 1
    assert result[0] == None

@pytest.mark.parametrize('arg', ['sdsfs', '34325.3424.2433', 'fsf3242sdfs'])
def test_div_wrong_argument(arg):
    with pytest.raises(TypeError):
        galgbra.div(arg)

@pytest.mark.parametrize('arg1, arg2', [(['dsad'], [343]), (['sfs23234fds'], [54.43]), (['32.2432.324'], ['43'])])
def test_mul_wrong_argument_2(arg1, arg2):
    assert cast(tuple[None],galgbra.div(arg1, arg2))[0] == None

def test_pwr():
    result = galgbra.pwr([12.2343, 45.34432, 0.4343, 45], [3.454332, '7.54332', -0.0324, 'fsdfs'], 3)
    expected = [5712.936, 3130994268200.96, 1.027, None]
    if result:
        for r, e in zip(result, expected):
            assert str(r) == str(e)
    else:assert False

def test_pwr_none():
    result = cast(tuple[None],galgbra.pwr(['sdad'], [12.3332]))
    assert len(result) == 1
    assert result[0] == None

@pytest.mark.parametrize('arg', ['sdsfs', '34325.3424.2433', 'fsf3242sdfs'])
def test_pwr_wrong_argument(arg):
    with pytest.raises(TypeError):
        galgbra.pwr(arg)

@pytest.mark.parametrize('arg1, arg2', [(['dsad'], [343]), (['sfs23234fds'], [54.43]), (['32.2432.324'], ['43'])])
def test_pwr_wrong_argument_2(arg1, arg2):
    assert cast(tuple[None],galgbra.pwr(arg1, arg2))[0] == None

def test_log():
    result = galgbra.log([12.2343, 4.34432, 0.4343, 45], [3.454332, '7.54332', -0.0324, 'fsdfs'], 3)
    expected = ['2.020', '0.727', None, None]
    if result:
        for r, e in zip(result, expected):
            assert str(r) == str(e)
    else:assert False

def test_log_none():
    result = cast(tuple[None],galgbra.log(['sdad'], [12.3332]))
    assert len(result) == 1
    assert result[0] == None

@pytest.mark.parametrize('arg', ['sdsfs', '34325.3424.2433', 'fsf3242sdfs'])
def test_log_wrong_argument(arg):
    with pytest.raises(TypeError):
        galgbra.log(arg)

@pytest.mark.parametrize('arg1, arg2', [(['dsad'], [343]), (['sfs23234fds'], [54.43]), (['32.2432.324'], ['43'])])
def test_log_wrong_argument_2(arg1, arg2):
    assert cast(tuple[None],galgbra.log(arg1, arg2))[0] == None
