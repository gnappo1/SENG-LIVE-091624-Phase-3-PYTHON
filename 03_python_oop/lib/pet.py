# !/usr/bin/env python3
# Defines the location of the Python interpreter
# See More => https://stackoverflow.com/a/7670338/8655247

# Classes

# 1. ✅ Create a Pet class
class Pet:
    all_ = []
    __slots__ = ["_name", "_species", "_breed", "_age"]

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            # if k in ("name", "species", "breed", "age"):
            setattr(self, k, v)
        type(self).all_.append(self)

    def __repr__(self):
        return f"""
            Species: {self.species or None}
            Breed: {self.breed or None}
        """

    def introduce(self):
        return f"Hello there, my name is {self.name}"

    def get_name(self):
        return self._name

    def set_name(self, name):
        if not isinstance(name, str):
            raise AttributeError("Name must be a string")
        elif len(name) < 2:
            raise AttributeError("Name must be at least 2 characters long")
        else:
            import ipdb; ipdb.set_trace()
            self._name = name

    name = property(get_name, set_name)
    
    def get_species(self):
        return self._species

    def set_species(self, species):
        if not isinstance(species, str):
            raise AttributeError("species must be a string")
        elif species.lower() not in ["dog", "cat"]:
            raise ValueError("species must be dog or cat")
        else:
            self._species = species

    species = property(get_species, set_species)
    
    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if not isinstance(breed, str):
            raise AttributeError("breed must be a string")
        elif len(breed) < 2:
            raise AttributeError("breed must be at least 2 characters long")
        else:
            self._breed = breed

    breed = property(get_breed, set_breed)
    
    def get_age(self):
        return self._age

    def set_age(self, age):
        if not isinstance(age, int):
            raise AttributeError("age must be an integer")
        elif age < 0:
            raise ValueError("age must be a positive integer")
        else:
            self._age = age

    age = property(get_age, set_age)

fido = Pet(name="fu", species="dog",breed= "labradoodle")
import ipdb; ipdb.set_trace()


# Use dot notation to access each Pet instance's attributes
# Update attributes with new values

# Instance Methods

