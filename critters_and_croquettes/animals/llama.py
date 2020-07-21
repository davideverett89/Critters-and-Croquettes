from animals import Animal
from movements import Walking

class Llama(Animal, Walking):
    
    def __init__(self, name, chip_number, species, shift, food):
        Animal.__init__(self, name, chip_number, species, food)
        Walking.__init__(self)
        self.shift = shift
