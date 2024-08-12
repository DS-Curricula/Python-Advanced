# Define the base class Animal
class Animal:
    # Method to make a generic animal sound
    def sound(self):
        print("Some generic animal sound.")


# Define the subclass Dog, inheriting from Animal
class Dog(Animal):
    # Method to make a specific sound for a dog
    def sound(self):
        print("Woof! Woof!")


# Define the subclass Cat, inheriting from Animal
class Cat(Animal):
    # Method to make a specific sound for a cat
    def sound(self):
        print("Meow! Meow!")


# Create an instance of the Animal class
animal = Animal()
# Call the sound method of the Animal class
animal.sound()  # Output: Some generic animal sound.

# Create an instance of the Dog class
dog = Dog()
# Call the sound method of the Dog class (overridden method)
dog.sound()  # Output: Woof! Woof!

# Create an instance of the Cat class
cat = Cat()
# Call the sound method of the Cat class (overridden method)
cat.sound()  # Output: Meow! Meow!
