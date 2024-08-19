from passlib.context import CryptContext

# Initialize CryptContext for bcrypt hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Generate bcrypt hashes for your passwords
print("Admin hashed password:", hash_password("adminpass"))  # Hash for admin
print("User hashed password:", hash_password("userpass"))    # Hash for user
