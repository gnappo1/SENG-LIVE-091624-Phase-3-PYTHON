from lib.pet import Pet

class Owner:
    all_ = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        # self.pets = []
        type(self).all_.append(self)

    def pets(self):
        return [pet for pet in Pet.all_ if pet.owner is self]