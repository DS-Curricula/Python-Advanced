# Creating a set using curly brackets
# my_set = {1,2,3}
# print(my_set)

# Creating a set from a list using the set() function
# my_set = set([4,5,6])
# print(my_set)

# #Creating an empty set using the set() function
# my_set = set()
# print(my_set)


my_set = {1, 2, 3, 3, 4, 5, 6}
print(my_set)  # Sets automatically remove duplicates

########################
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Compute union between set1 and set2 using the union() method
union_result_method = set1.union(set2)

# Compute union between set1 and set2 using the | operator
union_result_operator = set1 | set2

print("Union of set1 and set2 using union method: ", union_result_method)  # Output: {1,2,3,4,5}
print("Union of set1 and set2 using the | operator: ", union_result_operator)  # Output: {1,2,3,4,5}

# Compute intersection between set1 and set2 using the intersection() method
intersection_result_method = set1.intersection(set2)

# Compute intersection between set1 and set2 using the & operator
intersection_result_operator = set1 & set2

print("Intersection of set1 and set2 using intersection method: ", intersection_result_method)  # Output {3}
print("Intersection of set1 and set2 using the & opeator: ", intersection_result_operator)  # Output {3}

# Compute the elements that are unique to set1 using the difference method
difference_result_method = set1.difference(set2)

# Compute the elements that ar unique to set1 using the  - operator
difference_result_operator = set1 - set2

print("Difference of set1 and set2 using the difference method: ", difference_result_method)  # Output: {1,2}
print("Difference of set1 and set2 using the - operator: ", difference_result_operator)  # Output: {1,2}

# Compute the elements that are in set1 and set2 but not in their intersection
symmetric_difference_method = set1.symmetric_difference(set2)

# Compute the elements that are in set1 and set2 but not in their intersection using the ^ operator
symmetric_difference_operator = set1 ^ set2

print("Symmetric difference of set1 and set2 using symmetric_difference method: ", symmetric_difference_method)
# Output: {1,2,4,5}
print("Symmetric difference of set1 and set2 using the ^ operator: ", symmetric_difference_operator)
# Output: {1,2,4,5}


# SET METHODS


# Create a set
my_set = {1, 2, 3}

# Adding 7 to the end of the set
my_set.add(7)

# Removing 3 from the set
my_set.remove(3)

# Removing 8 from the set without throwing an error if 8 is now in the set
my_set.discard(8)

print(my_set)  # Output: {1,2,7}

# Removes all the elements
my_set.clear()

set_length = len(my_set)
print(set_length)  # Output: 0

# Removing duplicates from a list

# Create a list that contains duplicates
my_list = [1, 2, 3, 3, 4, 4, 5]

# Convert the list to a set to remove duplicates
unique_set = set(my_list)

# Convert the set back to a list
unique_list = list(unique_set)
print(unique_list)  # Output [1,2,3,4,5]

# Checking for common elements

user1_interests = {"music", "movies", "travel"}
user2_interests = {"movies", "reading", "cooking"}
common_interests = user1_interests.intersection(user2_interests)
print(common_interests)  # Output {"movies"}

# IN Operator
colors = {"red", "green", "blue"}
color = "green"
print(color in colors)  # Output: True
print(color not in colors)  # Output: False
