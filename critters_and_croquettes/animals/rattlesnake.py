from animals import Animal
from movements import Slithering

class Rattlesnake(Animal, Slithering):
    
    def __init__(self, name, chip_number, species, food):
        Animal.__init__(self, name, chip_number, species, food)
        Slithering.__init__(self)