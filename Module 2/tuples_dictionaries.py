# Creating a dictionary of student's grades using tuples as keys
grades = {
    ("John", "Math"): 5,
    ("Alice", "Biology"): 4,
    ("Bob", "Physics"): 3.5,
    ("Eve", "Music"): 5,
    ("John", "English"): 4
}

# Accessing John's grade in math
john_math = grades[("John", "Math")]
print("John's grade in math is ", john_math)

# Adding a new entry
grades[("Bob", "Math")] = 3
print(grades)

# Creating a list of dictionary keys
keys = list(grades.keys())

# Unpacking the first key of the dictionary which is a tuple
student, subject = keys[0]
print(student, "'s grade in ", subject, " is ", john_math)
