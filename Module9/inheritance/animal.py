class Animal:
    # Constructor to initialize species attribute
    def __init__(self, species):
        self.species = species

    # Method to make a generic animal sound
    def make_sound(self):
        print("Some generic animal sound...")


# Define the subclass Dog, inheriting from Animal
class Dog(Animal):
    # Constructor to initialize species and breed attributes
    def __init__(self, species, breed):
        # Call the superclass constructor to initialize the species attribute
        super().__init__(species)
        self.breed = breed

    # Method to make a specific sound for a dog
    def make_sound(self):
        print("Woof! Woof!")


# Example usage:
# Create an instance of the Animal class
animal = Animal("Canine")

# Create an instance of the Dog class
dog = Dog("Canine", "Golden Retriever")

# Call the make_sound method of the Animal class
animal.make_sound()  # Output: Some generic animal sound...

# Call the make_sound method of the Dog class
dog.make_sound()  # Output: Woof! Woof!


