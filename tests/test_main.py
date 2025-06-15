import pytest
from app.main import add

def test_add():
    assert add(2, 5) == 7
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

