from critters_and_croquettes.animals import Animal

class Frog(Animal):
    
    def __init__(self, name, chip_number, species, food):
        super().__init__(name, chip_number, species, food)
        self.isSwimming = True

    def feed(self):
        return f'{self.name} must meditate for 3 hours before feeding.'