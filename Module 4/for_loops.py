# Create a list of names
names = ["Alice", "Bob", "Charlie", "David"]

# Iterate in the names list and print every name
for name in names:
    print(name)
###############################


sentence = "Hello, World"

for character in sentence:
    if character.isalpha():  # CHeck if the character is a letter
        print(character)

# RANGE FUNCTION

for number in range(1, 6):  # prints number from the 1 to 5 (n, n-1):
    print(number)

numbers = [12, 45, 6, 72, 21, 8, 94, 57]

# Initialize a variable "maximum" with the first value from the list "numbers"
maximum = numbers[0]

for num in numbers:  # Begin a loop iterating through each element in the list "numbers"
    if num > maximum:  # Check if the current element "num" is greater than the current maximum value
        maximum = num  # If sp, update the maximum value to be the current element "num"
print("The maximum value in the list is:", maximum)