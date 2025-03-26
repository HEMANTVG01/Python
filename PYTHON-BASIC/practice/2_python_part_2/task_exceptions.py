"""
Write a function which divides x by y.
If y == 0 it should print "Division by 0" and return None
elif y == 1 it should raise custom Exception with "Deletion on 1 get the same result" text
else it should return the result of division
In all cases it should print "Division finished"
    >>> division(1, 0)
    Division by 0
    Division finished
    >>> division(1, 1)
    Division finished
    DivisionByOneException("Deletion on 1 get the same result")
    >>> division(2, 2)
    1
    Division finished
"""
import typing


def division(x: int, y: int) -> typing.Union[None, int]:
    ...

def division_error(x, y):
    if y == 0:
        print("Division by 0")
    elif y == 1:
        raise Exception("Deletion on 1 gets the same result")
    else:
        return x/y, "Division Finished"

try:
    print(division_error(2,0))
except:
    print("Division by zero")
try:
    print(division_error(2,1))
except Exception:
    print("Deletion on 1 gets the same result")
try:
    print(division_error(2,2))
except:
    print("Division Finished")
