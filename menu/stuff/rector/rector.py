from menu.stuff.person.person import Person


class Rector(Person):
    def __init__(self, name: str, surname: str, phoneNumber: int):
        super(Rector, self).__init__(name, surname, phoneNumber)