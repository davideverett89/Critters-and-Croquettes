class Wetlands:

    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = list()

    def add_animals(self, animal):
        self.animals.append(animal)

    def __str__(self):
        return f"{self.attraction_name}: {self.description}"