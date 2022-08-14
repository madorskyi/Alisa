from menu.stuff.student.student import Student
from menu.university.managmant.managemant import Managament


class Group(Managament):
    __students_list = []

    def __init__(self, name: str, title: str, description: str):
        super(Group, self).__init__(name, title, description)

    def add_new_student(self, student: Student):
        self.__students_list.append(student)

    def remove_student(self, student: Student):
        self.__students_list.remove(student)
