"""
Create 3 classes with interconnection between them (Student, Teacher,
Homework)
Use datetime module for working with date/time
1. Homework takes 2 attributes for __init__: tasks text and number of days to complete
Attributes:
    text - task text
    deadline - datetime.timedelta object with date until task should be completed
    created - datetime.datetime object when the task was created
Methods:
    is_active - check if task already closed
2. Student
Attributes:
    last_name
    first_name
Methods:
    do_homework - request Homework object and returns it,
    if Homework is expired, prints 'You are late' and returns None
3. Teacher
Attributes:
     last_name
     first_name
Methods:
    create_homework - request task text and number of days to complete, returns Homework object
    Note that this method doesn't need object itself
PEP8 comply strictly.
"""
import datetime


class Teacher:
    ...


class Student:
    ...


class Homework:
    ...


if __name__ == '__main__':
    teacher = Teacher('Dmitry', 'Orlyakov')
    student = Student('Vladislav', 'Popov')
    teacher.last_name  # Daniil
    student.first_name  # Petrov

    expired_homework = teacher.create_homework('Learn functions', 0)
    expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    expired_homework.deadline  # 0:00:00
    expired_homework.text  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    oop_homework.deadline  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late

#############################################################################################

import datetime

class Homework:
    def __init__(self, text, number_of_days):
        self.text = text
        self.deadline = datetime.timedelta(days= number_of_days)
        self.created = datetime.datetime.now()
    
    def is_active(self):
        current_date = self.created + self.deadline
        if datetime.datetime.now() <= current_date:
            return True
        else:
            return False

class Student(Homework):
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name
    
    def do_homework(self, homework):
        if homework.is_active():
            print(f"{self.first_name} {self.last_name} is doing homework")
        else:
            print(f"{self.first_name} {self.last_name}, You are too late")
        
class Teacher:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name
    
    def create_homework(self, text, number_of_days):
        return Homework(text, number_of_days)

if __name__ == "__main__":
    obj_Teacher = Teacher("Ram", "Kumar")
    print(obj_Teacher.last_name)
    print(obj_Teacher.first_name)

    obj_Teacher_homework = obj_Teacher.create_homework('Object Oriented Programming', 4)
    print(f"Homework created: {obj_Teacher_homework.text}")
    print(f"Deadline: {obj_Teacher_homework.deadline}")
    print(f"Created on: {obj_Teacher_homework.created}")

    obj_homework_Teacher = obj_Teacher.create_homework
    obj_homework = obj_homework_Teacher('Perform multiple Inheritance', 2)
    print(f"Homework created: {obj_homework.text}")
    print(f"Deadline: {obj_homework.deadline}")

    obj_expired_homework = obj_Teacher.create_homework
    obj_expired_task = obj_expired_homework("operators calculator", -1)
    print(f"Homework created: {obj_Teacher_homework.text}")
    print(f"Deadline: {obj_Teacher_homework.deadline}")
    print(f"created: {obj_Teacher_homework.created}")

    obj_Student = Student("Kumar", "Pradeep")
    obj_Student.do_homework(obj_homework)
    obj_Student.do_homework(obj_expired_task)

#####output##
Ram
Kumar
Homework created: Object Oriented Programming
Deadline: 4 days, 0:00:00
Created on: 2025-03-26 12:45:27.920169
Homework created: Perform multiple Inheritance
Deadline: 2 days, 0:00:00
Homework created: Object Oriented Programming
Deadline: 4 days, 0:00:00
created: 2025-03-26 12:45:27.920169
Pradeep Kumar is doing homework
Pradeep Kumar, You are too late
