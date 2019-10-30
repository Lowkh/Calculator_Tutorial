from my_calculator_functions import *

class MyCalculator(object):

    def __init__(self):
        self._answer = 0.0


    def last_answer(self):
        return self._answer

    def do_math(self, *arg, function):
        self._answer = function(*arg)
        return self._answer
    

    def add(self, *arg):
        return self.do_math(*arg, add)

    def subtract(self, *arg):
        return self.do_math(*arg, subtract)

    def multiply(self, *arg):
        return self.do_math(*arg, multiply)

    def divide(self, *arg):
        return self.do_math(*arg, divide)
