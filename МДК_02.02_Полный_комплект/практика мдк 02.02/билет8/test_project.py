from main_module import calculate
from helper_module import add

def test_add():
    assert add(2, 3) == 5

def test_calculate():
    assert calculate() == 5