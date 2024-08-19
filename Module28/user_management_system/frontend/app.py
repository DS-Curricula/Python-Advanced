import streamlit as st
import requests

API_URL = "http://localhost:8000"


def login(username, password):
    try:
        response = requests.post(f"{API_URL}/login", json={"username": username, "password": password})
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Invalid username or password")
            return None
    except requests.exceptions.RequestException:
        st.error("Could not connect to the backend")
        return None


def register(username, password, role):
    try:
        response = requests.post(f"{API_URL}/register", json={"username": username, "password": password, "role": role})
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Username already exists or invalid input")
            return None
    except requests.exceptions.RequestException:
        st.error("Could not connect to the backend")
        return None


def admin_register(admin_username, username, password, role):
    try:
        response = requests.post(f"{API_URL}/admin/register",
                                 json={"username": username, "password": password, "role": role},
                                 params={"username": admin_username})
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Failed to register user")
            return None
    except requests.exceptions.RequestException:
        st.error("Could not connect to the backend")
        return None


def get_users(username):
    try:
        response = requests.get(f"{API_URL}/users", params={"username": username})
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Could not fetch users")
            return None
    except requests.exceptions.RequestException:
        st.error("Could not connect to the backend")
        return None


def edit_user(user_id, username, role, admin_username):
    try:
        response = requests.put(f"{API_URL}/users/{user_id}", json={"username": username, "role": role},
                                params={"username": admin_username})
        if response.status_code == 200:
            st.success("User updated successfully")
        else:
            st.error("Failed to update user")
    except requests.exceptions.RequestException:
        st.error("Could not connect to the backend")


def delete_user(user_id, admin_username):
    try:
        response = requests.delete(f"{API_URL}/users/{user_id}", params={"username": admin_username})
        if response.status_code == 200:
            st.success("User deleted successfully")
        else:
            st.error("Failed to delete user")
    except requests.exceptions.RequestException:
        st.error("Could not connect to the backend")


def main():
    # Initialize session state variables
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.user_info = None

    # Check if the user is logged in
    if not st.session_state.logged_in:
        st.title("Streamlit Authentication with FastAPI and SQLite")

        menu = ["Login", "User Management"]
        choice = st.sidebar.selectbox("Menu", menu)

        if choice == "Login":
            st.sidebar.subheader("Login")
            username = st.sidebar.text_input("Username")
            password = st.sidebar.text_input("Password", type="password")
            login_button = st.sidebar.button("Login")

            if login_button:
                user_info = login(username, password)
                if user_info:
                    st.session_state.logged_in = True
                    st.session_state.user_info = user_info
                    st.sidebar.success(f"Welcome {user_info['username']}! Role: {user_info['role']}")

        elif choice == "Register":
            st.sidebar.subheader("Register")
            username = st.sidebar.text_input("Username")
            password = st.sidebar.text_input("Password", type="password")
            role = st.sidebar.selectbox("Role", ["user"])  # Users can only register as "user"
            register_button = st.sidebar.button("Register")

            if register_button:
                new_user = register(username, password, role)
                if new_user:
                    st.sidebar.success(f"User {new_user['username']} registered successfully!")

    else:
        user_info = st.session_state.user_info
        st.sidebar.success(f"Welcome {user_info['username']}! Role: {user_info['role']}")
        st.sidebar.button("Logout", on_click=lambda: logout())

        # Admin and user-specific navigation
        if user_info["role"] == "admin":
            admin_menu = st.sidebar.radio("Admin Menu", ["Manage Users", "Register New User"])

            if admin_menu == "Manage Users":
                st.header("Manage Users")
                manage_users_section(user_info["username"])

            elif admin_menu == "Register New User":
                st.header("Register New User")
                new_username = st.text_input("New Username")
                new_password = st.text_input("New Password", type="password")
                new_role = st.selectbox("Role", ["user", "admin"])
                if st.button("Register User"):
                    new_user = admin_register(user_info["username"], new_username, new_password, new_role)
                    if new_user:
                        st.success(f"User {new_user['username']} registered successfully!")

        elif user_info["role"] == "user":
            user_menu = st.sidebar.radio("User Menu", ["View Users", "Register New User"])

            if user_menu == "View Users":
                st.header("View Users")
                display_users_dashboard(user_info["username"])

            elif user_menu == "Register New User":
                st.header("Register New User")
                new_username = st.text_input("New Username")
                new_password = st.text_input("New Password", type="password")
                if st.button("Register User"):
                    new_user = register(new_username, new_password, "user")
                    if new_user:
                        st.success(f"User {new_user['username']} registered successfully!")


def display_users_dashboard(username):
    users = get_users(username)
    if users:
        st.subheader("All Users")
        for user in users:
            st.write(f"User: {user['username']} | Role: {user['role']}")


def manage_users_section(admin_username):
    users = get_users(admin_username)
    if users:
        for user in users:
            st.write(f"User: {user['username']} | Role: {user['role']}")

            # Create a unique key for each user form to avoid conflicts
            if st.button(f"Edit {user['username']}", key=f"edit_{user['id']}"):
                new_username = st.text_input(f"New Username for {user['username']}", value=user["username"],
                                             key=f"username_{user['id']}")
                new_role = st.selectbox(f"New Role for {user['username']}", ["user", "admin"],
                                        index=0 if user["role"] == "user" else 1, key=f"role_{user['id']}")

                if st.button(f"Save Changes for {user['username']}", key=f"save_{user['id']}"):
                    edit_user(user["id"], new_username, new_role, admin_username)
                    st.success(f"User {new_username} updated successfully!")

                    # Refresh the user data immediately after making changes
                    st.rerun()

            if st.button(f"Delete {user['username']}", key=f"delete_{user['id']}"):
                delete_user(user["id"], admin_username)
                st.success(f"User {user['username']} deleted successfully!")

                st.experimental_set_query_params(deleted="true")
                st.rerun()

def logout():
    st.session_state.logged_in = False
    st.session_state.user_info = None



if __name__ == "__main__":
    main()
