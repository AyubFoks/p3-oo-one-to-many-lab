class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError(
                f"Invalid pet type. Must be one of {Pet.PET_TYPES}")
        self.name = name
        self.pet_type = pet_type
        self.owner = None
        Pet.all.append(self)

        if owner:
            self.set_owner(owner)

    def set_owner(self, owner):
        """Assign an owner to this pet and add pet to owner's list"""
        if hasattr(owner, "add_pet"):
            self.owner = owner
            owner.add_pet(self)
        else:
            raise TypeError("Owner must have an add_pet method")


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Must be an instance of Pet")
        if pet not in self._pets:
            self._pets.append(pet)
            pet.owner = self

    def pets(self):
        return self._pets

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)
