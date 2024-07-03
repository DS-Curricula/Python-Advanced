alice = {
    "name": "Alice",
    "phone": "123-456-7890",
    "email": "alice@example.com"
}

bob = {
    "name": "Bob",
    "phone": "987-654-0321",
    "email": "bob@example.com"
}

contacts = {"Alice": alice, "Bob": bob}

#Printing Alice's Info
print("Alice's Contact Information")
print("Name:",contacts["Alice"]["name"])
print("Phone:",contacts["Alice"]["phone"])
print("Email:",contacts["Alice"]["email"])


#Update Alice's phone number
contacts["Alice"]["phone"] = "444-1234"
print("Alice's Contact Information")
print("Name:",contacts["Alice"]["name"])
print("Phone:",contacts["Alice"]["phone"])
print("Email:",contacts["Alice"]["email"])


#Printing Bob's Info
print("Bob's Contact Information")
print("Name:",contacts["Bob"]["name"])
print("Phone:",contacts["Bob"]["phone"])
print("Email:",contacts["Bob"]["email"])
