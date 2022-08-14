from abc import ABC


class Managament(ABC):
    def __init__(self, name: str, title: str, description: str):
        self.name = name
        self.title = title
        self.description = description

    def __str__(self):
        return f"{self.name} - {self.title} - {self.description}"
