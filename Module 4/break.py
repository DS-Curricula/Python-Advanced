numbers = [1, 2, 3, 4, 5, 6]
target = 4

for number in numbers:
    print(number) #Print the current element being iterated
    if number == target: #Check if the current element is equal to the target value
        print("Target found!")
        break #Exit the loop immediately after finding the target value