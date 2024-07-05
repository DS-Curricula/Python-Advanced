# tuple example
words = ("spam", "eggs", "sausages")

# Access the items using indexing
print(words[0])

# empty tuple
empty_tuple = ()
print(empty_tuple)

# Try to reassign a value and ask the student about their output (they would get an error)
# words[1] = "cheese"


# Creating a tuple with information about a person
person = ("Alice", 30, "Engineer")
# Tuple unpacking
name, age, profession = person
# Printing the information about person
print(name, "'s", " profession is", profession, "and she is", age, "years old.")
