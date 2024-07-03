#Conditionals

age = 18

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")

#Output will be "You can vote".


#Nested Conditionals

temperature = 28

if temperature >30:
    print("It's a hot day, stay hydrated")
elif 20 <= temperature <=30:
    print("The weather is pleasant")
else:
    print("It's a cold day, bundle up")


#Create a program that checks if a number is even or odd

number = 7

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


#Create input for users

user_input = input("Enter a number")
number = int(user_input)

#Check if the number is positive, negative or zero

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")