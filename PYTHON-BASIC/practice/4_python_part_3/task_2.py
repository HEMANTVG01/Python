"""
Write function which executes custom operation from math module
for given arguments.
Restrition: math function could take 1 or 2 arguments
If given operation does not exists, raise OperationNotFoundException
Examples:
     >>> math_calculate('log', 1024, 2)
     10.0
     >>> math_calculate('ceil', 10.7)
     11
"""
import math


def math_calculate(function: str, *args):
    ...


"""
Write tests for math_calculate function
"""
##Solution##
import math

class OperationNotFoundException(Exception):
    pass

def math_calculate(a, b, c):
    try:
        result_log = math.log(a, b)  
        result_ceil = math.ceil(c)
        return result_log, result_ceil
    except ValueError:
        raise OperationNotFoundException(f"The Operation cannot be performed with values: a={a}, b={b}, c={c}")

print(math_calculate(1024, 2, 10.7))  
