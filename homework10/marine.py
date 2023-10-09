"""
Creating new class of Marine Animals that inherits Animal class
Creating subclass Fish that inherits Marine Animal
Creating subclass Shark that inherits Fish class
"""

from animal import Animal


class MarineAnimal(Animal):
    _type = "MarineAnimal"

    def __init__(self, name, species, habitat):
        super().__init__(name, species)
        self.habitat = habitat

    def swim(self):
        return f"{self.name} is swimming in the {self.habitat} habitat."


class Fish(MarineAnimal):
    def __init__(self, name, species, habitat, fins):
        super().__init__(name, species, habitat)
        self.fins = fins

    def breathe_underwater(self):
        return f"{self.name} can breathe underwater using its {self.fins} fins."


class Shark(Fish):
    def __init__(self, name, species, fins):
        super().__init__(name, species, "ocean", fins)

    def hunt(self):
        return f"{self.name} is hunting for prey in the ocean."
