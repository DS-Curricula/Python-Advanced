class Person:
    def __init__(self, name, age):
        # Initialize a Person object with a name and age
        self.name = name
        self.age = age

    def greet(self):
        # Method to greet with name and age
        print(f"Hello, I am {self.name}, and I am {self.age} years old.")


# Create two Person instances
person1 = Person("Alice", 15)
person2 = Person("Bob", 17)

# Greet each person
person1.greet()  # Output: Hello, I am Alice, and I am 15 years old.
person2.greet()  # Output: Hello, I am Bob, and I am 17 years old.
