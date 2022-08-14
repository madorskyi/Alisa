from menu.stuff.person.person import Person


class Dean(Person):
    def __init__(self, name: str, surname: str, about: str, phoneNumber: int):
        super(Dean, self).__init__(name, surname, phoneNumber)
        self.about = about