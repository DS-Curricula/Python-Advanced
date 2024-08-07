from pydantic import BaseModel
from typing import Optional


# Base model for Recipe with all required fields and optional fields
class RecipeBase(BaseModel):
    name: str
    description: Optional[str] = None
    ingredients: str
    instructions: str
    cuisine: str
    difficulty: str
    category_id: Optional[int] = None


# Model for creating a new recipe, which includes all fields from RecipeBase
class RecipeCreate(RecipeBase):
    pass


# Model for a recipe with an ID, inheriting from RecipeBase
class Recipe(RecipeBase):
    id: int
