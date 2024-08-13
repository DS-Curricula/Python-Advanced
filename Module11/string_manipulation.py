# Reading and Processing Lines
with open('example.txt', 'r') as file:
    for line in file:
        cleaned_line = line.strip() # Remove leading/trailing whitespace
        print(cleaned_line)

# Splitting Lines into Words
with open("example.txt", "r") as file:
    for line in file:
        words = line.strip().split() # Split line into words
        print(words)

# Concatenating Strings
name = "Alice"
age = 30

with open("output.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + str(age) + "\n")

# Formatting Strings
with open("output.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")


# Read, process and write data
with open("example.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        cleaned_line = line.strip() # Remove leading/trailing whitespace
        modified_line = cleaned_line.replace("Line 1", "Line X") # Replace text
        outfile.write(modified_line + "\n") # Write modified to output file
