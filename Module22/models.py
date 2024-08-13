from pydantic import BaseModel, FieldValidationInfo, field_validator, constr, conint

# User model with validation
class User(BaseModel):
    id: int
    name: str
    age: int

    @field_validator('age')
    def age_must_be_positive(cls, v, info: FieldValidationInfo):
        if v <= 0:
            raise ValueError('Age must be positive')
        return v

# Example Usage
try:
    user = User(id=1, name="John Doe", age=-1)
except ValueError as e:
    print(e)
    
# Address model to be used in User model
class Address(BaseModel):
    street: str
    city: str

# Another user model with different validation rules
class another_user(BaseModel):
    id: conint(gt=0)  # id must be greater than 0
    name: constr(min_length=2, max_length=50)  # name length must be between 2 and 50

