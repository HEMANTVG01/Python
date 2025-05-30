"""
Write tests for division() function in 2_python_part_2/task_exceptions.py
In case (1,1) it should check if exception were raised
In case (1,0) it should check if return value is None and "Division by 0" printed
If other cases it should check if division is correct

TIP: to test output of print() function use capfd fixture
https://stackoverflow.com/a/20507769
"""


def test_division_ok(capfd):
    ...


def test_division_by_zero(capfd):
    ...


def test_division_by_one(capfd):
    ...


### Solution ###
import pytest

def division_error(x, y):
    if y == 0:
        print("Division by 0")
    elif y == 1:
        raise Exception("Deletion on 1 gets the same result")
    else:
        return x / y, "Division Finished"

def test_division_by_zero():
    result = division_error(2, 0)
    assert result is None

def test_division_by_one():
    with pytest.raises(Exception) as exc_info:
        division_error(2, 1)
    assert str(exc_info.value) == "Deletion on 1 gets the same result"

def test_valid_division():
    result = division_error(2, 2)
    assert result == (1.0, "Division Finished")
