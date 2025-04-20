"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""
#####
import pytest
import datetime
from p2task1 import Homework, Student, Teacher

def test_homework_is_active():
    hw = Homework("Test HW", 1)
    assert hw.is_active() == True

def test_homework_expired():
    hw = Homework("Old HW", -1)
    assert hw.is_active() == False

def test_teacher_creation():
    teacher = Teacher("Doe", "John")
    assert teacher.last_name == "Doe"
    assert teacher.first_name == "John"

def test_teacher_create_homework():
    teacher = Teacher("Smith", "Alice")
    hw = teacher.create_homework("OOP Concepts", 3)
    assert isinstance(hw, Homework)
    assert hw.text == "OOP Concepts"
    assert hw.deadline == datetime.timedelta(days=3)

def test_student_can_do_active_homework(capfd):
    student = Student("Kumar", "Pradeep")
    hw = Homework("Active HW", 2)
    student.do_homework(hw)
    out, _ = capfd.readouterr()
    assert "Pradeep Kumar is doing homework" in out

def test_student_cannot_do_expired_homework(capfd):
    student = Student("Kumar", "Pradeep")
    hw = Homework("Expired HW", -2)
    student.do_homework(hw)
    out, _ = capfd.readouterr()
    assert "Pradeep Kumar, You are too late" in out
