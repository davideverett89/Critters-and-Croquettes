from datetime import date

# Petting Area

class Llama:
    
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.dated_added = date.today()
        self.isWalking = True

class Goat:
    
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.dated_added = date.today()
        self.isWalking = True

class Pig:
    
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.dated_added = date.today()
        self.isWalking = True

class Rabbit:
    
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.dated_added = date.today()
        self.isWalking = True

class GiantTortoise:
    
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.dated_added = date.today()
        self.isWalking = True

# Glass Tank Area

class PythonSnake:
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.dated_added = date.today()
        self.isSlithering = True

class CopperheadSnake:
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.dated_added = date.today()
        self.isSlithering = True

class RatSnake:
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.dated_added = date.today()
        self.isSlithering = True

class RattleSnake:
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.dated_added = date.today()
        self.isSlithering = True

class GarterSnake:
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.dated_added = date.today()
        self.isSlithering = True

# Pond Area

class Goldfish:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.isSwimming = True

class MallardDuck:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.isSwimming = True

class Catfish:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.isSwimming = True

class LargemouthBass:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.isSwimming = True

class Frog:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.isSwimming = True

steve = Llama('Steve', 'Llama', 'morning')
frank = Goat('Frank', 'Goat', 'evening')
bob = Pig('Bob', 'Pig', 'midday')
jeff = Rabbit('Jeff', 'Rabbit', 'evening')
george = GiantTortoise('George', 'Giant Tortoise', 'midday')

pete = PythonSnake('Pete', 'Python')
rodger = CopperheadSnake('Rodger', 'Copperhead')
maxwell = RatSnake('Maxwell', 'Rat Snake')
terrence = RattleSnake('Terrence', 'Rattlesnake')
mary = GarterSnake('Mary', 'Garter Snake')

reginald = Goldfish('Reginald', 'Goldfish')
katie = MallardDuck('Katie', 'Mallard Duck')
jessica = Catfish('Jessica', 'Catfish')
betty = LargemouthBass('Betty', 'Largemouth Bass')
bertha = Frog('Bertha', 'Frog')

# Putting them in a list and looping through it just for fun:

petting_zoo = [steve, frank, bob, jeff, george, pete, rodger, maxwell, terrence, mary, reginald, katie, jessica, betty, bertha]

petting_area_animals = list()

for animal in petting_zoo:
    if hasattr(animal, 'isWalking'):
        petting_area_animals.append(animal)

for animal in petting_area_animals:
    print(f'{animal.name} the {animal.species} is available to pet during the {animal.shift} shift.')