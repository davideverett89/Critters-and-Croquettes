from animals import Animal
from movements import Swimming

class Frog(Animal, Swimming):
    
    def __init__(self, name, chip_number, species, food):
        Animal.__init__(self, name, chip_number, species, food)
        Swimming.__init__(self)

    def feed(self):
        return f'{self.name} must meditate for 3 hours before feeding.'