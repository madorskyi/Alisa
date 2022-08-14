from menu.university.facultys.faculty import Faculty
from menu.university.managmant.managemant import Managament


class Departament(Managament):
    __group_faculties = []

    def __init__(self, name: str, title: str, description: str):
        super(Departament, self).__init__(name, title, description)

    def add_new_faculties(self, faculty: Faculty):
        self.__group_faculties.append(faculty)

    def remove_faculties(self, faculty: Faculty):
        self.__group_faculties.remove(faculty)

