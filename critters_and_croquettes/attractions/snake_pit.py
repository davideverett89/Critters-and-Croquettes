from attractions import Attraction

class SnakePit(Attraction):

    def __init__(self, attraction_name, description):
        super().__init__(attraction_name, description)

    def add_animal(self, animal):
        try:
            if hasattr(animal, 'slither_speed'):
                self.animals.append(animal)
        except AttributeError as ex:
            print(f'{animal.name} could potentially be eaten, so please do not put it in the {self.attraction_name} attraction.')