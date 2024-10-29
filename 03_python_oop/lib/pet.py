# !/usr/bin/env python3
# Defines the location of the Python interpreter
# See More => https://stackoverflow.com/a/7670338/8655247

#! YAGNI
import ipdb

# Classes

# 1. ✅ Create a Pet class
class Pet:
    # _name -> protected attributes
    # __name -> private attributes
    # __name__ -> dunder or magic methods
    # name_ -> use a trailing underscore to avoid collision/overriding python reserved keywords
    def __init__(self, **kwargs):
        #! Mass Assignment
        for k, v in kwargs.items():
            if (k in ["name", "species", "breed", "temperament", "owner", "age"]):
                setattr(self, k, v)
        # self.name = pet_name
        # self.age = age
        # self.breed = breed
        # self.species = species
        # self.temperament = temperament
        # self.owner = owner

    # Note: Add 'pass' to the Pet class
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if not isinstance(name, str):
            raise AttributeError("Name must be a string")
        elif not name:
            raise AttributeError("Name must be a string with at least one character")
        self._name = name
    
    name = property(get_name, set_name)

    def say_hello(self):
        """This is a comment, specifically a documentation for a method"""
        return f"Hello there, my name is {self.name}!"
    
    def __repr__(self):
        return f"""
            Pet:
              Name: {self.name}
              Species: {self.species}
              Breed: {self.breed}
              Temperament: {self.temperament}
              Owner: {self.owner}
        """

#! Instantiation: creating an object out of a specific class
fido = Pet(
    name="Fido",
    species="dog",
    breed="husky",
    temperament="diva",
    owner="Matteo",
    age=0,
)
milo = Pet(
    species="cat",
    breed="siamese",
    temperament="lazy",
    owner="Marco",
    age=3,
    pet_name="Milo",
)
import ipdb; ipdb.set_trace()
fido.say_hello()
milo.say_hello()

# 2. ✅ Instantiate a few Pet instances

# Compare the Pet instances. Are each of them the same object?

# 3. ✅ Demonstrate __init__

# Add arguments to instances

# Attributes:
# name
# age
# breed
# temperament
# owner

# Use dot notation to access each Pet instance's attributes

# Update attributes with new values

# Instance Methods

# 4. ✅ Create a "print_pet_details" function that will print each Pet instance's
# attributes

# Review the "self" keyword

# Invoke "print_pet_details" on an instance

# Example Terminal Ouput:
# name: Rose
# age: 11
# breed: Domestic Longhair
# temperament: Sweet

# 5. ✅ Create an Owner class with two instance methods:

# get_name => Retrieve Owner's name

# set_name => Set Owner's name

# Ensure that Owner's name is a String

# If not, issue warning of "Name must be a string"

# Use property() to compile get_name / set_name and invoke them
# whenever we access an Owner instance's name

# Object Properties => Attributes that are controlled by methods
