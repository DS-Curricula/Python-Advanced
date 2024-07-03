#Dictionary

contant_info = {"Alice": "555-1234", "Bob": "555-5678"}
print(contant_info)


alica_phone = contant_info["Alice"]
print(alica_phone)
#This will print the value of the key "Alica: that is 555-1234

#Update Alice's number
contant_info["Alice"] = "555-6789"
print(contant_info)

#Add Eve's number by specifying her key and value
contant_info["Eve"] = "555-9999"
print(contant_info)
#the outcome should look like this {'Alice': '555-6789', 'Bob': '555-5678', 'Eve': '555-9999'}

#Delete Bob's contact from the dictionary
del contant_info["Bob"]
print(contant_info)

#Get the keys fro the contact_info dictionary
keys = contant_info.keys()
print(keys)
#the outcome: dict_keys(['Alice', 'Eve'])


#Get the values from the contact_info dictionary
values = contant_info.values()
print(values)
#the outcome: dict_values(['555-6789', '555-9999'])


#Get the items (key - value) pairs from the contact_info dictionary
items = contant_info.items()
print(items)
#the outcome: dict_items([('Alice', '555-6789'), ('Eve', '555-9999')])


#Creating a dictionary to store contact information for different people
#Each key in this dictionary is a person's name
#and the corresponding value is another disctionary containing various pices of contact information

contant_information = {
    #Alice's information stored in a dictionary
    "Alice" : {
        "phone_number": "555-1234",
        "email": "alice@gmail.com",
        "home_address": "123 Main St, Cityville",
        "birthday": "20/11/2000"
    },
    # Bob's information stored in a dictionary
    "Bob": {
        "phone_number": "555-5678",
        "email": "bob@gmail.com",
        "home_address": "456 Main St, Cityville",
        "birthday": "15/09/1997"
    },
    # Alice's information stored in a dictionary
    "Eve": {
        "phone_number": "555-9999",
        "email": "eve@gmail.com",
        "home_address": "789 Main St, Cityville",
        "birthday": "05/03/2001"
    }
}

print(contant_information)

#Getting the inner dictionary for Bob and assign it to the variable bob_information
bob_information = contant_information["Bob"]
print(bob_information)



# Creating a dictionary of contact information using tuples
contacts = {
    "Alice": ("555-1234", "alice@gmail.com"),
    "Bob": ("555-5678", "bob@gmail.com"),
    "Eve": ("555-9999", "eve@gmail.com")
}

#Accessing Alice's phone and email
alice_info = contacts["Alice"]
phone_number = alice_info[0]
print(phone_number)
email = alice_info[1]
print(email)

#Alternatively, you can use tuple unpacking for a more readable syntax:
phone_number, email = contacts["Alice"]