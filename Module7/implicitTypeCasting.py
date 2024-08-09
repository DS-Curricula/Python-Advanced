# Example 1

x = 32
y = 5.3

result = x + y
print(result, "of type", type(result))  # Output: 37.3 of type <class 'float'>

age = 25
message = "I am " + str(age) + " years old"
print(message)  # Output: I am 25 years old.

a = 5
b = "3"
result1 = a * int(b)
print(result1, "of type", type(result1))  # Output: 15 of type <class 'int'>

# Raises a ValueError: Invalid literal for int() with base 10: 'abc'
# z = int("abc")
