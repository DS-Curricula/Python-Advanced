#First way

#import my_math
#esult = my_math.square(5) # Using the entire module
#print(result)


#Second way

from my_math import square
result = square(5) #Using the function imported directly
print(result)