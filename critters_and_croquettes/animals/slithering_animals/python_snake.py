from datetime import date

class PythonSnake:
    
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.dated_added = date.today()
        self.isSlithering = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
            return f"{self.name} is a {self.species}"