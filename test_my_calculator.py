import pytest
from mycalculator.my_calculator_functions import *


def test_subtract():
    value = subtract(1,2,3)
    assert value == -4

def test_subtract_positive_negative():
    value = subtract(1,-2,3)
    assert value == 0

def test_subtract_negative_negative():
    value = subtract(-1,-2)
    assert value == 1

def test_over_ten_variables():
    value = subtract(1,2,3,4,5,6,7,8,9,10,11)
    assert value == "Error: >10 Values"
