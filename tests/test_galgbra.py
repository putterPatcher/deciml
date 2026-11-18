import pytest
from ..deciml.deciml import galgbra
from typing import cast

def test_add():
    result = galgbra.add([12.33542, 23.267632, 'dsfsfs'], [23.25443, 34.3, '4.343'], ['43.3453', 6.343222, '34'], pr=3)
    expected = [78.935, 63.911, None]
    if result:
        for r, e in zip(result, expected):
            assert str(r) == str(e)
    else:assert False

def test_add_none():
    result = cast(tuple[None],galgbra.add(['sdad'], [12.3332]))
    assert len(result) == 1
    assert result[0] == None



