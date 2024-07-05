# Your challenge code here

# Function definition
def myfunc(n):
    return  lambda a : a * n

# Creating instances
mydoubler = myfunc(2)
mytripler = myfunc(3)

#Using instances
result_doubler = mydoubler(11)
result_tripler = mytripler(11)

#Output
print("Double of 11:", result_doubler) #Output: 22
print("Triple of 11:", result_tripler) #Output: 33