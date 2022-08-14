from menu.stuff.person.person import Person


class Manager(Person):
    def __init__(self , name: str, surname: str, phoneNumber: int):
        super(Manager, self).__init__(name, surname, phoneNumber)