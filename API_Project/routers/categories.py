import sqlite3
from typing import List
from streamlit import status
from models.category import Category, CategoryCreate
from database import get_db_connection
from fastapi import APIRouter, HTTPException

# Create an APIRouter instance for category-related routes
router = APIRouter()


# Route to retrieve all categories
@router.get("/categories/", response_model=List[Category])
def get_categories():
    """
    Retrieve all categories from the database.

    This endpoint fetches all categories and their details from the database and
    returns them as a list of Category objects.

    Returns:
        List[Category]: A list of Category objects representing all categories in the database.
    """
    # Establish a database connection
    conn = get_db_connection()
    cursor = conn.cursor()
    # Execute SQL query to fetch all categories
    cursor.execute("SELECT id, name FROM categories")
    categories = cursor.fetchall()
    conn.close()

    # Convert the list of tuples into a list of Category dictionaries
    category_list = [{"id": cat[0], "name": cat[1]} for cat in categories]
    return category_list


# Route to create a new category
@router.post("/categories/", response_model=Category)
def create_category(category: CategoryCreate):
    """
    Create a new category in the database.

    This endpoint inserts a new category into the database with the provided
    name. If the category already exists, it raises a conflict error.

    Returns:
        Category: The created Category object with its generated ID.

    Raises:
        HTTPException: 409 Conflict if the category already exists.
        HTTPException: 500 Internal Server Error for other exceptions.
    """
    # Establish a database connection
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Execute SQL query to insert a new category
        cursor.execute("INSERT INTO categories (name) VALUES (?)", (category.name,))
        conn.commit()
        category_id = cursor.lastrowid
        return Category(id=category_id, name=category.name)
    except sqlite3.IntegrityError:
        # Handle case where the category already exists
        conn.close()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"The category '{category.name}' already exists."
        )
    except Exception as e:
        # Handle other exceptions
        conn.close()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {e}"
        )
    finally:
        # Ensure the database connection is closed
        conn.close()


# Route to update an existing category by ID
@router.put("/categories/{category_id}", response_model=Category)
def update_category(category_id: int, category: CategoryCreate):
    """
    Update the name of an existing category.

    This endpoint updates the name of a category identified by its ID. If the
    category ID does not exist, it raises a 404 error.

    Returns:
        Category: The updated Category object.

    Raises:
        HTTPException: 404 Not Found if the category ID does not exist.
    """
    # Establish a database connection
    conn = get_db_connection()
    cursor = conn.cursor()
    # Execute SQL query to update the category name
    cursor.execute("UPDATE categories SET name = ? WHERE id = ?", (category.name, category_id))
    if cursor.rowcount == 0:
        # Handle case where the category ID does not exist
        conn.close()
        raise HTTPException(status_code=404, detail="Category not found")
    conn.commit()
    conn.close()
    return Category(id=category_id, name=category.name)


# Route to delete a category by ID
@router.delete("/categories/{category_id}", response_model=dict)
def delete_category(category_id: int):
    """
    Delete a category from the database by ID.

    This endpoint deletes a category identified by its ID. If the category ID does
    not exist, it raises a 404 error.

    Returns:
        dict: A dictionary with a detail message indicating the category has been deleted.

    Raises:
        HTTPException: 404 Not Found if the category ID does not exist.
    """
    # Establish a database connection
    conn = get_db_connection()
    cursor = conn.cursor()
    # Execute SQL query to delete the category
    cursor.execute("DELETE FROM categories WHERE id = ?", (category_id,))
    if cursor.rowcount == 0:
        # Handle case where the category ID does not exist
        conn.close()
        raise HTTPException(status_code=404, detail="Category not found")
    conn.commit()
    conn.close()
    return {"detail": "Category deleted"}
