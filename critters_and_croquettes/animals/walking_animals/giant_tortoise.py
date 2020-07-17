from datetime import date

class GiantTortoise:
    
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.dated_added = date.today()
        self.isWalking = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
            return f"{self.name} is a {self.species}"