from pydantic import BaseModel, conint, constr
from typing import Optional

# class User(BaseModel):
#     id: int
#     name: str
#     age: int
#     email: str

# user = User(id=1, name='John Doe', age=30, email='john.doe@example.com')



# Define the User class with optional fields
class User(BaseModel):
    id: int
    name: str
    age: Optional[int] = None
    email: Optional[str] = None

# Define another_user class with constraints
class another_user(BaseModel):
    id: conint(gt=0)  # id must be greater than 0
    name: constr(min_length=2, max_length=50)  # name length must be between 2 and 50

# Create instances of User and print them
user1 = User(id=1, name="Alice", age=25, email="alice@example.com")
print(user1)

user2 = User(id=2, name="Bob", email="bob@example.com")
print(user2)

user3 = User(id=3, name="Charlie", age=30)
print(user3)

user4 = User(id=4, name="Dana")
print(user4)

# Create instances of another_user and print them
valid_user = another_user(id=1, name="Alice")
print(valid_user)

# The following instance is invalid and should raise a validation error if uncommented
# invalid_user1 = another_user(id=0, name="Alice")
# print(invalid_user1)
