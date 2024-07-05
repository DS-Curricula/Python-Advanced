class Vertebrate:
    def __init__(self, backbone=True):
        self.has_backbone = backbone


    def vertebrate_info(self):
        print("Vertebrates have a backbone.")


class Aquatic:
    def __init__(self, habitat="water"):
        self.habitat = habitat

    def aquatic_info(self):
        print("Aquatic animals live in water.")


class Fish(Vertebrate, Aquatic):
    def __init__(self, species, backbone=True, habitat="water"):
        super().__init__(backbone=backbone)
        self.habitat = habitat
        self.species = species

    def fish_info(self):
        print(f"The {self.species} is a type of fish found in {self.habitat}.")

    def swim(self):
        print("The fish is swimming.")


# Example usage
goldfish = Fish("Goldfish")
print(goldfish.has_backbone)  # Output: True (Inherited from Vertebrate)
print(goldfish.habitat)  # Output: water (Inherited from Aquatic)
goldfish.vertebrate_info()  # Output: Vertebrates have a backbone.
goldfish.aquatic_info()  # Output: Aquatic animals live in water.
goldfish.fish_info()  # Output: The Goldfish is a type of fish found in water.
goldfish.swim()  # Output: The fish is swimming.
