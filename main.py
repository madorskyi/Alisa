import re

from menu.stuff.rector.rector import Rector
from menu.stuff.student.student import Student
from menu.stuff.dean.dean import Dean
from menu.stuff.manager.manager import Manager
from menu.stuff.teacher.teacher import Teacher
from menu.university.department.department import Departament
from menu.university.facultys.faculty import Faculty
from menu.university.groups.group import Group

s = Student('StudentRoman', 'Student-Roman', '1243456789')
s.show()

# s = Manager('Manger-Viktoria', 'Manger-Viktoria', '1243456789')
# s.show()
# #
# d = Dean('Dean-Miroslav', 'Dean-Miroslav', 'PROFESSIONAL DEAN', '1243456789')
# d.show()
#
# t = Teacher('Teacher-Ekaterina', 'Teacher-Ekaterina', '1243456789')
# t.show()
# #
# r = Rector('RectorElena', 'Rector-Elena', '1243456789')
# r.show()
#
# g = Group('Group', 'Group-Title', 'Group-Description')
# print(g)
#
# de = Departament('Departament', 'Departament-Title', 'Departament-Description')
# print(de)
#
# f = Faculty('Faculty', 'Faculty-Title', 'Faculty-Description')
# print(f)
