"""
Generic class for all animals
"""


class Animal:
    _type = "Animal"

    def __init__(self, name, species):
        self.name = name
        self.species = species

    """
    All animals can eat
    """

    def eat(self):
        return f"{self.name} is eating."

    """
    All animals can sleep
    """

    def sleep(self):
        return f"{self.name} is sleeping."

    """
    Protected method of existing 
    """

    def _existing(self):
        return f"{self.name} is existing"


class Mammal(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color

    def give_birth(self):
        return f"{self.name} is giving birth to live young."


class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

    def fly(self):
        return f"{self.name} is flying with a wingspan of {self.wingspan} inches."
