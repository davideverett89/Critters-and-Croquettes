from datetime import date
import threading

# Petting Area

class Llama:
    
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

class Goat:
    
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

class Pig:
    
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

class Rabbit:
    
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

# Glass Tank Area

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

class CopperheadSnake:
    
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

class RatSnake:
    
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

class RattleSnake:
    
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

class GarterSnake:
    
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

# Pond Area

class Goldfish:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.isSwimming = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
            return f"{self.name} is a {self.species}"

class MallardDuck:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.isSwimming = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
            return f"{self.name} is a {self.species}"

class Catfish:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.isSwimming = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
            return f"{self.name} is a {self.species}"

class LargemouthBass:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.isSwimming = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
            return f"{self.name} is a {self.species}"

class Frog:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.isSwimming = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
            return f"{self.name} is a {self.species}"

steve = Llama('Steve', 'Llama', 'morning', 'oats')
frank = Goat('Frank', 'Goat', 'evening', 'oats')
bob = Pig('Bob', 'Pig', 'midday', 'slop')
jeff = Rabbit('Jeff', 'Rabbit', 'evening', 'carrots')
george = GiantTortoise('George', 'Giant Tortoise', 'midday', 'cabbage')

pete = PythonSnake('Pete', 'Python', 'dead rat')
rodger = CopperheadSnake('Rodger', 'Copperhead', 'dead rat')
maxwell = RatSnake('Maxwell', 'Rat Snake', 'dead rat')
terrence = RattleSnake('Terrence', 'Rattlesnake', 'small child')
mary = GarterSnake('Mary', 'Garter Snake', 'dead rat')

reginald = Goldfish('Reginald', 'Goldfish', 'fish food')
katie = MallardDuck('Katie', 'Mallard Duck', 'bread')
jessica = Catfish('Jessica', 'Catfish', 'fish food')
betty = LargemouthBass('Betty', 'Largemouth Bass', 'fish food')
bertha = Frog('Bertha', 'Frog', 'flies')

# Putting them in a list and looping through it just for fun:

petting_zoo = [steve, frank, bob, jeff, george, pete, rodger, maxwell, terrence, mary, reginald, katie, jessica, betty, bertha]

petting_area_animals = list()

for animal in petting_zoo:
    if hasattr(animal, 'isWalking'):
        petting_area_animals.append(animal)

for animal in petting_area_animals:
    print(f'{animal.name} the {animal.species} is available to pet during the {animal.shift} shift.')

def feedAnimals(animal_list):
    for animal in animal_list:
        animal.feed()

def runFeedAnimals():
    feedAnimals(petting_zoo)

def set_interval(func, sec): 
    def func_wrapper():
        set_interval(func, sec) 
        func()  
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

set_interval(runFeedAnimals, 5)