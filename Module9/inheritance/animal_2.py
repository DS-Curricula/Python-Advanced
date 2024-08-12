# Define the base class Animal
class Animal:
    # Constructor to initialize the name attribute
    def __init__(self, name):
        self.name = name

    # Method to make a generic animal sound
    def sound(self):
        print("Some generic animal sound.")

    # Method to provide a basic description of the animal
    def description(self):
        print(f"This is an animal named {self.name}.")


# Define the subclass Dog, inheriting from Animal
class Dog(Animal):
    # Constructor to initialize name and breed attributes
    def __init__(self, name, breed):
        # Call the superclass constructor to initialize the name attribute
        super().__init__(name)
        self.breed = breed

    # Method to make a specific sound for a dog
    def sound(self):
        print("Woof! Woof!")

    # Method to provide a description of the dog
    def description(self):
        # Call the description method of the parent class Animal
        super().description()
        # Add specific information for Dog
        print(f"Breed: {self.breed}")


# Define the subclass Cat, inheriting from Animal
class Cat(Animal):
    # Constructor to initialize name and color attributes
    def __init__(self, name, color):
        # Call the superclass constructor to initialize the name attribute
        super().__init__(name)
        self.color = color

    # Method to make a specific sound for a cat
    def sound(self):
        print("Meow! Meow!")

    # Method to provide a description of the cat
    def description(self):
        # Call the description method of the parent class Animal
        super().description()
        # Add specific information for Cat
        print(f"Color: {self.color}")


# Example usage:
# Create an instance of the Animal class
animal = Animal("Generic Animal")
# Call the sound method of the Animal class
animal.sound()  # Output: Some generic animal sound.
# Call the description method of the Animal class
animal.description()  # Output: This is an animal named Generic Animal.

# Create an instance of the Dog class
dog = Dog("Rex", "Golden Retriever")
# Call the sound method of the Dog class (overridden method)
dog.sound()  # Output: Woof! Woof!
# Call the description method of the Dog class (calls parent class method and adds its own)
dog.description()  # Output: This is an animal named Rex. Breed: Golden Retriever

# Create an instance of the Cat class
cat = Cat("Whiskers", "Black")
# Call the sound method of the Cat class (overridden method)
cat.sound()  # Output: Meow! Meow!
# Call the description method of the Cat class (calls parent class method and adds its own)
cat.description()  # Output: This is an animal named Whiskers. Color: Black
