class Pet:
    all_ = []

    def __init__(self, name, breed, owner): #! make sure that owner is a full Owner object
        self.name = name
        self.breed = breed
        self.owner = owner #! SSoT (dependency injection)
        type(self).all_.append(self)

    def __getattr__(self, attr):
        #! this method is invoked only when the attribute doesn't exist
        #! trying to override the default behavior of returning an AttributeError
        return None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            #! 1. print a error message
            # ! 2. return None or an error message
            #! 3. raise an error/exception
            # return "Name must be of type string"
            raise TypeError("Name must be of type string")
        elif not new_name:
            raise ValueError("Names must be at least one char long")
        else:
            self._name = new_name

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, new_breed):
        if not isinstance(new_breed, str):
            raise TypeError("Breed must be of type string")
        elif not new_breed:
            raise ValueError("Breeds must be at least one char long")
        else:
            self._breed = new_breed

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner_instance):
        from lib.owner import Owner
        if not isinstance(owner_instance, Owner):
            raise TypeError("Owner must be of type Owner")
        self._owner = owner_instance


# matteo = Owner("matteo", "piccini")
# pet = Pet(7, "husky", matteo)
# import ipdb; ipdb.set_trace()
