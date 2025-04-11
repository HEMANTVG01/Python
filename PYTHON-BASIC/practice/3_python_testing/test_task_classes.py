"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""
#####
import pytest
import datetime
from time import sleep

from your_module_name import Homework, Student, Teacher  # replace with actual module name

def test_homework_creation():
    hw = Homework("Test Homework", 3)
    assert hw.text == "Test Homework"
    assert isinstance(hw.deadline, datetime.timedelta)
    assert hw.deadline.days == 3
    assert isinstance(hw.created, datetime.datetime)

def test_homework_is_active():
    hw_active = Homework("Active Homework", 1)
    assert hw_active.is_active() is True

    # Creating homework with negative deadline, should be inactive
    hw_expired = Homework("Expired Homework", -1)
    assert hw_expired.is_active() is False

def test_teacher_create_homework():
    teacher = Teacher("Doe", "John")
    hw = teacher.create_homework("Learn Python", 2)
    assert isinstance(hw, Homework)
    assert hw.text == "Learn Python"
    assert hw.deadline.days == 2

def test_student_do_homework_active(capsys):
    student = Student("Smith", "Anna")
    hw = Homework("Write Essay", 1)
    student.do_homework(hw)
    
    captured = capsys.readouterr()
    assert "Anna Smith is doing homework" in captured.out

def test_student_do_homework_expired(capsys):
    student = Student("Sharma", "Ravi")
    hw = Homework("Old Task", -2)
    student.do_homework(hw)
    
    captured = capsys.readouterr()
    assert "Ravi Sharma, You are too late" in captured.out
