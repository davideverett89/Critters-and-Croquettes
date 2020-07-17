from critters_and_croquettes import Llama, Goat, Pig, Rabbit, GiantTortoise
from critters_and_croquettes import PythonSnake, CopperheadSnake, RatSnake, Rattlesnake, GarterSnake
from critters_and_croquettes import Goldfish, MallardDuck, Catfish, LargemouthBass, Frog

from critters_and_croquettes import PettingZoo
from critters_and_croquettes import SnakePit
from critters_and_croquettes import Wetlands

varmint_village = PettingZoo("Varmint Village", "A place to pet and feed some cuddly critters!")
slither_inn = SnakePit("Slither Inn", "A place to check out some creepy snakes!")
critter_cove = Wetlands("Critter Cove", "Come hang out with our aquatic friends!")

steve = Llama('Steve', 'Llama', 'morning', 'oats')
sharon = Llama('Sharon', 'Llama', 'evening', 'oats')
frank = Goat('Frank', 'Goat', 'evening', 'oats')
darlene = Goat('Darlene', 'Goat', 'morning', 'oats')
bob = Pig('Bob', 'Pig', 'midday', 'slop')
randy = Pig('Randy', 'Pig', 'evening', 'slop')
jeff = Rabbit('Jeff', 'Rabbit', 'evening', 'carrots')
george = GiantTortoise('George', 'Giant Tortoise', 'midday', 'cabbage')

pete = PythonSnake('Pete', 'Python', 'dead rat')
rodger = CopperheadSnake('Rodger', 'Copperhead', 'dead rat')
maxwell = RatSnake('Maxwell', 'Rat Snake', 'dead rat')
terrence = Rattlesnake('Terrence', 'Rattlesnake', 'small child')
mary = GarterSnake('Mary', 'Garter Snake', 'dead rat')

reginald = Goldfish('Reginald', 'Goldfish', 'fish food')
katie = MallardDuck('Katie', 'Mallard Duck', 'bread')
jessica = Catfish('Jessica', 'Catfish', 'fish food')
betty = LargemouthBass('Betty', 'Largemouth Bass', 'fish food')
bertha = Frog('Bertha', 'Frog', 'flies')

petting_zoo_animals = [steve, sharon, darlene, randy, frank, bob, jeff, george, pete, rodger, maxwell, terrence, mary, reginald, katie, jessica, betty, bertha]
petting_zoo_attractions = [varmint_village, slither_inn, critter_cove]

def assignAnimals(animals_list):
    for animal in animals_list:
        if hasattr(animal, 'isWalking'):
            varmint_village.add_animals(animal)
        elif hasattr(animal, 'isSlithering'):
            slither_inn.add_animals(animal)
        elif hasattr(animal, 'isSwimming'):
            critter_cove.add_animals(animal)


def report_to_terminal():
    assignAnimals(petting_zoo_animals)
    for attraction in petting_zoo_attractions:
        print(f"""
{attraction} Allow me to introduce them:
_________________________________________________________________________________
""")
        for animal in attraction.animals:
            print(f"* {animal}")


report_to_terminal()