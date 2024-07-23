# Create dictionaries for Jane and John to store contact information
jane_contact = {
    'name': 'Jane',
    'phone': '123-456-7890',
    'email': 'jane@example.com'
}

john_contact = {
    'name': 'John',
    'phone': '987-654-3210',
    'email': 'john@example.com'
}

# Create a contacts dictionary and add Jane and John
contacts = {
    'Jane': jane_contact,
    'John': john_contact
}

# Print Jane's contact information
print("Jane's contact information:")
print(contacts['Jane'])

# Update Jane's phone number
contacts['Jane']['phone'] = '111-222-3333'

# Print Jane's updated contact information
print("\nJane's updated contact information:")
print(contacts['Jane'])