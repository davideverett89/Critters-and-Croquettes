from datetime import date

class Llama:
    
    def __init__(self, name, chip_number, species, shift, food):
        self.name = name
        self.__chip_number = chip_number
        self.species = species
        self.shift = shift
        self.food = food
        self.dated_added = date.today()
        self.isWalking = True

    @property
    def chip_number(self):
        return self.__chip_number

    @chip_number.setter
    def chip_number(self, number):
        pass

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
            return f"{self.name} is a {self.species}"