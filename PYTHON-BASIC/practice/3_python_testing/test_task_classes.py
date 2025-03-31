"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""


import datetime

class Homework:
    def __init__(self, text, number_of_days):
        self.text = text
        self.deadline = datetime.timedelta(days=number_of_days)
        self.created = datetime.datetime.now()

    def is_active(self):
        current_date = self.created + self.deadline
        return datetime.datetime.now() <= current_date


class Student:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework):
        if homework.is_active():
            print(f"{self.first_name} {self.last_name} is doing homework: {homework.text}")
        else:
            print(f"{self.first_name} {self.last_name}, You are too late for homework: {homework.text}")


class Teacher:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(self, text, number_of_days):
        return Homework(text, number_of_days)
