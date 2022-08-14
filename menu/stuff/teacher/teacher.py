from menu.stuff.person.person import Person
from menu.stuff.student.student import Student


class Teacher(Person):

    def __init__(self, name: str, surname: str, phoneNumber: int):
        super(Teacher, self).__init__(name, surname, phoneNumber)

    def set_marks_to_student(self, student: Student):
        pass

