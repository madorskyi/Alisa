from menu.stuff.person.person import Person


class Student(Person):
    marks = { 'Teacher': [1, 2, 3, 4, 5, 6, ]}

    def __init__(self, name: str, surname: str, phoneNumber: int):
        super(Student, self).__init__(name, surname, phoneNumber)

    def show(self):
        super(Student, self).show()
        print(f' List  \t\t\t {self.marks}')
