#Write a program that calculates the sum of even numbers from 1 to 10

#Initialize a variable to store the total sum
total = 0

#Iterate through numbers from 1 to 10
for number in range(1, 11):
    #Check if the number is even
    if number % 2 == 0:
        #Add the even number to the total sum
        total += number

#Print the result
print("The sum of even numbers from 1 to 10 is:",total)