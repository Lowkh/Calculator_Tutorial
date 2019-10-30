import pytest
from mycalculator.my_calculator_functions import *


def test_multiply():
    value = multiply(1,2,3)
    assert value == 6

def test_multiply_positive_negative():
    value = multiply(1,-2,3)
    assert value == -6

def test_multiply_negative_negative():
    value = multiply(-1,-2)
    assert value == 2

def test_over_ten_variables():
    value = multiply(1,2,3,4,5,6,7,8,9,10,11)
    assert value == "Error: >10 Values"
