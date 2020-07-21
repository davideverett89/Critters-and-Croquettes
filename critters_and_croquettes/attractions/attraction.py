class Attraction:

    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    @property
    def last_animal_added(self):
        last_animal = self.animals[-1]
        return last_animal

    def __str__(self):
        return f'{self.attraction_name} is home to {len(self)} animals.'

    def __len__(self):
        return len(self.animals)