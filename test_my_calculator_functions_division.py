import pytest
from mycalculator.my_calculator_functions import *


def test_division():
    value = divide(2,2,3)
    assert value == 0.3333333333333333

def test_division_positive_negative():
    value = divide(1,-2)
    assert value == -0.5

def test_division_negative_negative():
    value = divide(-1,-2)
    assert value == 0.5

def test_division_by_zero():
    value = divide(10,0)
    assert value == ZeroDivisionError
    
def test_over_ten_variables():
    value = divide(1,2,3,4,5,6,7,8,9,10,11)
    assert value == "Error: >10 Values"
