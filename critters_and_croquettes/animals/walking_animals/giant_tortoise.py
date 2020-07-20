from critters_and_croquettes.animals import Animal

class GiantTortoise(Animal):
    
    def __init__(self, name, chip_number, species, shift, food):
        super().__init__(name, chip_number, species, food)
        self.shift = shift
        self.isWalking = True

    def feed(self):
        return f'{self.name} needs to be sung a sweet lullaby before feeding'