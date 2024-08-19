from pydantic import BaseModel, conint, constr
from typing import Optional

# class User(BaseModel):
#     id: int
#     name: str
#     age: int
#     email: str

# user = User(id=1, name='John Doe', age=30, email='john.doe@example.com')



# Modifying the previous model
class User(BaseModel):
    id: int
    name: str
    age: int = 0  # Default value if age is not provided
    email: str = "noemail@example.com" # Default value if email is not provided

# Create instances of User and print them
user1 = User(id=2, name="Jane Doe", email="janedoe@example.com")
print(user1)

user2 = User(id=3, name="Alice", age=25)
print(user2)

user4 = User(id=4, name="Bob")
print(user4)

# Define another_user class with constraints
class another_user(BaseModel):
    id: conint(gt=0)  # id must be greater than 0
    name: constr(min_length=2, max_length=50)  # name length must be between 2 and 50



# Create instances of another_user and print them
valid_user = another_user(id=1, name="Alice")
#print(valid_user)

# The following instance is invalid and should raise a validation error if uncommented
# invalid_user1 = another_user(id=0, name="Alice")
# print(invalid_user1)
