class Dog:
    def __init__(self, name):
        self.name = name

    # Method to make the dog sound
    def sound(self):
        print(f"{self.name} makes the sound: Woof!")


class Cat:
    def __init__(self, name):
        self.name = name

    # Method to make the cat sound
    def sound(self):
        print(f"{self.name} makes the sound: Meow!")


class Bird:
    def __init__(self, name):
        self.name = name

    # Method to make the bird sound
    def sound(self):
        print(f"{self.name} makes the sound: Chirp!")


# Create instances of each class
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweetie")

# Demonstrate polymorphism by calling the sound method on instances of different classes
for animal in (dog, cat, bird):
    animal.sound()

# Output of the program:
# Buddy makes the sound: Woof!
# Whiskers makes the sound: Meow!
# Tweetie makes the sound: Chirp!
