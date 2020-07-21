from animals import Animal
from movements import Swimming, Walking

class MallardDuck(Animal, Swimming, Walking):
    
    def __init__(self, name, chip_number, species, food):
        Animal.__init__(self, name, chip_number, species, food)
        Swimming.__init__(self)
        Walking.__init__(self)