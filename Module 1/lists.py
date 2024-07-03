to_do_list = ["math homework", "research for biology", "clean the room", "fun"]
first_item = to_do_list[0] #Accesses the first item at index 0, which is "math homework"
second_item = to_do_list[1] #Accesses the second at index 1, which is "research for biology"
third_item = to_do_list[2] #Accesses the third index 2, which is "clean the room"
fourth_item = to_do_list[3]#Accesses the fourth index 3, which is "fun"

print(first_item)
print(second_item)
print(third_item)
print(fourth_item)

shopping_list = ["apples", "bananas", 3, 4.5] #different data types

#Adding "oranges" to the end of the list
shopping_list.append("oranges")
print(shopping_list)

#Adding "lemons to the third position of the list"
shopping_list.insert(2, "lemons")
print(shopping_list)

#Removing data from "to_do_list

#Removing "research for biology" by specifying its value
to_do_list.remove("research for biology")
print(to_do_list)

#now the list is ['math homework', 'clean the room', 'fun']

#Removing the item at index 2, which is "fun"
del to_do_list[2]
print(to_do_list)

#Update Values

to_do_list[0] = "physics homework"
print(to_do_list)



