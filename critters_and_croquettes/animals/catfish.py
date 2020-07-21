from animals import Animal
from movements import Swimming

class Catfish(Animal, Swimming):
    
    def __init__(self, name, chip_number, species, food):
        Animal.__init__(self, name, chip_number, species, food)
        Swimming.__init__(self)