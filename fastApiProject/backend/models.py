from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., description="The name of the item")
    description: str = Field(None, description="The description of the item")
    price: float = Field(..., gt=0, description="The price of the item")
    tax: float = Field(None, description="The tax on the item")
