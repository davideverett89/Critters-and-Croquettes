from animals import Animal
from movements import Walking, Swimming

class Goose(Animal, Walking, Swimming):

    def __init__(self, name, chip_number, species, food):
        Animal.__init__(self, name, chip_number, species, food)
        Swimming.__init__(self)
        Walking.__init__(self)

    def run(self):
        print(f'{self} waddles')
    
    def honk(self): 
        print("The goose honks. A lot")

    def __str__(self):
        return f'{self.name} the Goose'