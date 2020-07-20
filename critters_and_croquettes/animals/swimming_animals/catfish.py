from critters_and_croquettes.animals import Animal

class Catfish(Animal):
    
    def __init__(self, name, chip_number, species, food):
        super().__init__(name, chip_number, species, food)
        self.isSwimming = True