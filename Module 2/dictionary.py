# Dictionary

contact_info = {"Alice": "555-1234",
                "Bob": "555-5678"
                }
#Create a variable called alice_phone and by using [] we can specify which key we want to access
alica_phone = contact_info["Alice"]
#Now let's print alice_phone
print(alica_phone)

# Result will be "555-1234"

# Update Alice's number
contact_info["Alice"] = "555-6789"
print(contact_info)

# Add Eve's number by specifying her key and value
contact_info["Eve"] = "555-9999"
print(contact_info)
# the output should look like this {'Alice': '555-6789', 'Bob': '555-5678', 'Eve': '555-9999'}

# Delete Bob's contact from the dictionary
del contact_info["Bob"]
print(contact_info)

# Get the keys from the contact_info dictionary
keys = contact_info.keys()
print(keys)
# the outcome: dict_keys(['Alice', 'Eve'])


# Get the values from the contact_info dictionary
values = contact_info.values()
print(values)
# the outcome: dict_values(['555-6789', '555-9999'])


# Get the items (key - value) pairs from the contact_info dictionary
items = contact_info.items()
print(items)
# the outcome: dict_items([('Alice', '555-6789'), ('Eve', '555-9999')])


# Creating a dictionary to store contact information for different people
# Each key in this dictionary is a person's name
# and the corresponding value is another dictionary containing various pieces of contact information

contact_information = {
    # Alice's information stored in a dictionary
    "Alice": {
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

print(contact_information)

# Getting the inner dictionary for Bob and assign it to the variable bob_information
bob_information = contact_information["Bob"]
print(bob_information)

# Creating a dictionary of contact information using tuples
contacts = {
    "Alice": ("555-1234", "alice@gmail.com"),
    "Bob": ("555-5678", "bob@gmail.com"),
    "Eve": ("555-9999", "eve@gmail.com")
}

# Accessing Alice's phone and email
alice_info = contacts["Alice"]
phone_number = alice_info[0]
print(phone_number)
email = alice_info[1]
print(email)

# Alternatively, you can use tuple unpacking for a more readable syntax:
phone_number, email = contacts["Alice"]
