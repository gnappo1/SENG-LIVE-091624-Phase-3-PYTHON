# import ipdb

# 7. ✅. Create a subclass of Pet called Cat
# import Pet from lib.pet

from pet import Pet

# 7. ✅. Create a subclass of Pet called Cat
class A:
    def test(self):
        print("Inside A")
class B:
    def test(self):
        print("Inside B")


# import Pet from lib.pet
class Cat(Pet, B, A): #! Mixins
    all_ = []
    # 8. ✅. Create Cat class + __init__ that takes all the parameters from Pet and an
    # additional parameter called indoor (Boolean)

    # Use super to pass the Pet parameters to the super class (DRY)

    # Add an indoor attribute

    def __init__(self, outdoor, **kwargs):
        #! do what the parent init does + one more thing
        super().__init__(**kwargs)
        self.outdoor = outdoor

    # 9. ✅. Create a method unique to the Cat subclass called talk which returns the string "Meow!"

    def meow(self):
        pass

    # 10. ✅. Create a method called print_pet_details to match the print_pet_details in Pet

    # Add super().print_pet_details() and print the indoor attribute
    def print_pet_details(self):
        pass

spidey = Cat(
    True, name="Fido", age=2, breed="siamese", temperament="docile", owner="Matteo"
)
tommy = Cat(
    False, name="Tommy", age=2, breed="siamese", temperament="docile", owner="Matteo"
)

print("done")
