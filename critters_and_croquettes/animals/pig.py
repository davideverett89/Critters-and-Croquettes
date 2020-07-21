from animals import Animal
from movements import Walking

class Pig(Animal, Walking):
    
    def __init__(self, name, chip_number, species, shift, food):
        Animal.__init__(self, name, chip_number, species, food)
        Walking.__init__(self)
        self.shift = shift

    def feed(self):
        return f'{self.name} must roll around in mud before he/she is ready to eat.'