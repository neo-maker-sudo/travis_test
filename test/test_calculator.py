import pytest
from calculator import Calculator

def test_add():
    x,y = 1,2
    instance = Calculator(x,y)
    assert instance.add() == x + y, "Add method wrong"

def test_subtract():
    x,y = 1,2
    instance = Calculator(x,y)
    assert instance.subtract() == x - y, "subtract method wrong"
