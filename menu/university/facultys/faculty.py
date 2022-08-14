from menu.university.groups.group import Group
from menu.university.managmant.managemant import Managament


class Faculty(Managament):
    __group_list = []

    def __init__(self, name: str, title: str, description: str):
        super(Faculty, self).__init__(name, title, description)

    def add_new_group(self, group: Group):
        self.__group_list.append(group)

    def remove_group(self, group: Group):
        self.__group_list.remove(group)