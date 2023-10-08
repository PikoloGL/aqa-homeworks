from animal import Animal

"""
Generic class for FlyingAnimals that inherits Animal class
"""


class FlyingAnimal(Animal):
    _type = "Flying Animal"

    def __init__(self, name, species, altitude):
        super().__init__(name, species)
        self.altitude = altitude

    """
    All flying animals can soar
    """

    def soar(self):
        return f"{self.name} is soaring at an altitude of {self.altitude} feet."

    @property
    def type(self):
        return self._type


"""
Class for bats, that inherits Flying animals
"""


class Bat(FlyingAnimal):
    def __init__(self, name, species, altitude, echolocation):
        super().__init__(name, species, altitude)
        self.echolocation = echolocation

    """
    Bats can navigate in the darkness
    """

    def navigate_in_darkness(self):
        return f"{self.name} uses echolocation to navigate in the dark while flying at {self.altitude} feet."


"""
Class for Eagles, that inherits Flying animals
"""


class Eagle(FlyingAnimal):
    def __init__(self, name, species, altitude, beak_type):
        super().__init__(name, species, altitude)
        self.beak_type = beak_type

    """
    Eagles can hunt
    """

    def hunt(self):
        return f"{self.name} is hunting for prey using its {self.beak_type} beak while flying at {self.altitude} feet."


"""
Usage of your flying classes
"""
if __name__ == "__main__":
    """
    Example of Eagle:
    Inheritance pass Animal -> Flying Animal -> Eagle
    """
    white_eagle = Eagle("White eagle", "Bird", 1000, "straight")  # We created an instance of Eagle
    print(white_eagle.name + " is a " + white_eagle.type)  # We check eagle`s type (inherited from FlyingAnimal)
    print(white_eagle.hunt())  # Eagle can hunt (method of Eagle's class)
    print(white_eagle.sleep())  # Eagle can sleep (inherited from Animal)
