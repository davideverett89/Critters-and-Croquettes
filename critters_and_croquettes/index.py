from animals import Goose, Catfish, CopperheadSnake, Frog, GarterSnake, GiantTortoise, Goat, Goldfish, LargemouthBass, Llama, MallardDuck, Pig, PythonSnake, Rabbit, RatSnake, Rattlesnake
from attractions import PettingZoo, SnakePit, Wetlands

varmint_village = PettingZoo("Varmint Village", "A place to pet and feed some cuddly critters!")
slither_inn = SnakePit("Slither Inn", "A place to check out some creepy snakes!")
critter_cove = Wetlands("Critter Cove", "Come hang out with our aquatic friends!")

steve = Llama('Steve', 1234567, 'Llama', 'morning', 'oats')
sharon = Llama('Sharon', 32165467, 'Llama', 'evening', 'oats')
frank = Goat('Frank', 1111111111, 'Goat', 'evening', 'oats')
darlene = Goat('Darlene', 222222222, 'Goat', 'morning', 'oats')
bob = Pig('Bob', 333333333333, 'Pig', 'midday', 'slop')
randy = Pig('Randy', 44444444444, 'Pig', 'evening', 'slop')
jeff = Rabbit('Jeff', 555555555555, 'Rabbit', 'evening', 'carrots')
george = GiantTortoise('George', 6666666666, 'Giant Tortoise', 'midday', 'cabbage')

pete = PythonSnake('Pete', 77777777777, 'Python', 'dead rat')
rodger = CopperheadSnake('Rodger', 8888888888888, 'Copperhead', 'dead rat')
maxwell = RatSnake('Maxwell', 99999999999, 'Rat Snake', 'dead rat')
terrence = Rattlesnake('Terrence', 1010101010101010, 'Rattlesnake', 'small child')
mary = GarterSnake('Mary', 1212121212121212, 'Garter Snake', 'dead rat')

reginald = Goldfish('Reginald', 131313131313, 'Goldfish', 'fish food')
katie = MallardDuck('Katie', 141414141414, 'Mallard Duck', 'bread')
jessica = Catfish('Jessica', 151515151515, 'Catfish', 'fish food')
betty = LargemouthBass('Betty', 161616161616, 'Largemouth Bass', 'fish food')
bertha = Frog('Bertha', 171717171717, 'Frog', 'flies')

becky = Goose('Becky', 6666666666, 'Goose', 'seeds')

print('Becky:', becky)
becky.run()
becky.swim()

steve.chip_number = 3333333333
print('Llama number:', steve.chip_number)

petting_zoo_animals = [steve, sharon, darlene, randy, frank, bob, jeff, george, pete, rodger, maxwell, terrence, mary, reginald, katie, jessica, betty, bertha]
petting_zoo_attractions = [varmint_village, slither_inn, critter_cove]

def assignAnimals(animals_list):
    for animal in animals_list:
        if hasattr(animal, 'walk_speed'):
            varmint_village.add_animal(animal)
        elif hasattr(animal, 'slither_speed'):
            slither_inn.add_animal(animal)
        elif hasattr(animal, 'swim_speed'):
            critter_cove.add_animal(animal)

varmint_village.add_animal(becky)


def report_to_terminal():
    assignAnimals(petting_zoo_animals)
    print('Last animal in varmint village:', varmint_village.last_animal_added)
    for attraction in petting_zoo_attractions:
        print(f"{attraction} Allow me to introduce them:")
        for animal in attraction.animals:
            print(f"* {animal}")

print('Pig feeding:',randy.feed())
print('Frog feeding:', bertha.feed())
print('Giant tortoise feeding:', george.feed())
print('Feeding all others:', maxwell.feed())


report_to_terminal()