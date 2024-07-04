#Example 1

age = 25

#Convert the integer 'age' to a string and assign it to 'age_as_str'
age_as_str = str(age)

print(age_as_str, "of type", type(age_as_str)) #Output: 25 of type <class 'str'>


#Example 2

#Casting integers into to bool
print(bool(0)) # Output: False
print(bool(42)) #Output: True

#Casting strings to bool
print(bool("")) #Output: False
print(bool("Hello")) #Output: True
#Casting lists to bool
print(bool([])) #Output: False

print(bool(None)) #Output: False
