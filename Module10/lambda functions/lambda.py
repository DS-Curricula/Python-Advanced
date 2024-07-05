# Regular function
def add(x,y):
    return x + y

#Equivalent lambda function
lambda_add = lambda x, y: x + y

#Usage
result1 = add(3, 5)
result2 = lambda_add(3,5)

print(result1) #Output: 8
print(result2) #Output: 8