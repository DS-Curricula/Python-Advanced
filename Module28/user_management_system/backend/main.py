from fastapi import FastAPI, HTTPException
from .models import UserCreate, UserLogin, AuthenticatedUser, UserUpdate, UserView
from .crud import create_user, get_user_by_username, get_all_users, update_user, delete_user
from .auth import authenticate_user, get_current_user

app = FastAPI()


@app.post("/login", response_model=AuthenticatedUser)
def login(user: UserLogin):
    authenticated_user = authenticate_user(user.username, user.password)
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return authenticated_user


@app.post("/register", response_model=AuthenticatedUser)
def register(user: UserCreate):
    if get_user_by_username(user.username):
        raise HTTPException(status_code=400, detail="Username already exists")

    # Force the role to "user" when registered by a regular user
    if user.role != "user":
        raise HTTPException(status_code=403, detail="You are not allowed to set this role.")

    create_user(user)
    return {"username": user.username, "role": user.role}


@app.post("/admin/register", response_model=AuthenticatedUser)
def admin_register(user: UserCreate, username: str):
    admin_user = get_current_user(username)
    if not admin_user or admin_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admins can register users with a custom role.")

    if get_user_by_username(user.username):
        raise HTTPException(status_code=400, detail="Username already exists")

    create_user(user)
    return {"username": user.username, "role": user.role}


@app.get("/users", response_model=list[UserView])
def list_users(username: str):
    user = get_current_user(username)
    if not user:
        raise HTTPException(status_code=401, detail="User not authenticated")

    if user["role"] == "admin" or user["role"] == "user":
        return get_all_users()
    else:
        raise HTTPException(status_code=403, detail="Access forbidden")


@app.put("/users/{user_id}")
def edit_user(user_id: int, user: UserUpdate, username: str):
    admin_user = get_current_user(username)
    if not admin_user or admin_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admins can edit users")
    update_user(user_id, user)
    return {"message": "User updated successfully"}


@app.delete("/users/{user_id}")
def delete_user_route(user_id: int, username: str):
    admin_user = get_current_user(username)
    if not admin_user or admin_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admins can delete users")
    delete_user(user_id)
    return {"message": "User deleted successfully"}
