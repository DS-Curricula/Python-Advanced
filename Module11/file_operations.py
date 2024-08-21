# Opening and Closing Files
# Open a file in 'read' mode
# file_path = "example.txt"
# file = open(file_path, "r")
#
# # Read the contents of the file
# content = file.read()
# print(content)

# Close the file
# file.close()

import os

# Opening and Closing Files
file = open('example.txt', 'r')
file.close()

# Using with statement for automatic closing
with open('example.txt', 'r') as file:
    content = file.read()

# File Modes
# 'r': Read (default mode)
# 'w': Write
# 'a': Append
# 'b': Binary mode (e.g., 'rb', 'wb')
# 'x': Exclusive creation

# Reading from Files
with open('example.txt', 'r') as file:
    content = file.read()  # Read entire content
    line = file.readline()  # Read a single line
    lines = file.readlines()  # Read all lines into a list

# Writing to Files
with open('example.txt', 'w') as file:
    file.write('Hello, World!')  # Write data to a file

lines = ['Hello, World!\n', 'Welcome to Python!\n']
with open('example.txt', 'w') as file:
    file.writelines(lines)  # Write multiple lines

# Moving the Cursor
with open('example.txt', 'r') as file:
    file.seek(0)  # Moves the cursor to the beginning of the file
    data = file.read()
    print(data)

# Checking File Existence
if os.path.exists('example.txt'):
    print('File exists')

# Appending to Files
with open("example.txt", "a") as file:
    file.write("New data appended.")

# Reading and Writing Binary Files

data = b'This is some binary data'
with open('example.bin', 'wb') as file:
    file.write(data)

with open('example.bin', 'rb') as binary_file:
    data = binary_file.read()





