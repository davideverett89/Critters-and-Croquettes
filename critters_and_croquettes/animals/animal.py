from datetime import date

class Animal:

    def __init__(self, name, chip_number, species, food):
        self.name = name
        self.__chip_number = chip_number
        self.species = species
        self.food = food
        self.date_added = date.today()

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