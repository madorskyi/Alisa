from abc import ABC
from datetime import datetime
from enum import Enum
import re


class Person(ABC):
    # region Logic
    @classmethod
    class __Role(Enum):
        Student = 'student'
        Teacher = 'teacher'
        Manager = 'manager'
        Rector = 'rector'
        Dean = 'dean'

    @classmethod
    def __whoIs(cls, object):
        from menu.stuff.student.student import Student
        from menu.stuff.manager.manager import Manager
        from menu.stuff.dean.dean import Dean
        from menu.stuff.rector.rector import Rector

        from menu.stuff.teacher.teacher import Teacher
        if isinstance(object, Student):
            return Person.__Role.Student
        elif isinstance(object, Manager):
            return Person.__Role.Manager
        elif isinstance(object, Dean):
            return Person.__Role.Dean
        elif isinstance(object, Rector):
            return Person.__Role.Rector
        elif isinstance(object, Teacher):
            return Person.__Role.Teacher

    @classmethod
    def __input_controllers(self, name):
        if not name.isalpha():
            print("Incorrect")
        else:
            print("Correct")

    @classmethod
    def __number_validation(self, number):
        regex = re.compile("\w{3}-\w{3}-\w{5}")

        if number.isdigit() and len(str(number)) == 10:
            if re.search(regex, number):
                print("Incorrect")
                return 0
            else:
                print("Correct")
                return format(int(number[:-1]), ",").replace(",", "-") + number[-1]

        else:
            print("Incorrect number input")

    # region Initialization

    def __init__(self, name: str, surname: str, phoneNumber: int):
        Person.__input_controllers(name)
        self.phoneNumber = Person.__number_validation(phoneNumber)

        self.name = name
        self.surname = surname
        self.role = Person.__whoIs(self)
        __time_tmp = datetime.now()
        self.created = __time_tmp.strftime('%Y-%m-%d')
        self.list_student = [] if self.role == Person.__Role.Teacher else None

    # endregion

    # region toString any Object

    def show(self):
        print(f' Name: \t\t\t {self.name} ' \
              f'\n Surname:  \t\t {self.surname} ' \
              f'\n PhoneNumber:  \t {self.phoneNumber} ' \
              f'\n Role: \t\t\t [{self.role.name}] ' \
              f'\n Created: \t\t {self.created}')
        if self.role == Person.__Role.Teacher:
            print(f' Student List: \t {self.list_student if len(self.list_student) > 0 else "Empty List"}')



    # endregion
