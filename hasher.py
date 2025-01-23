import hashlib

def hash_password(password, salt=""):
    # Combine password and salt
    salted_password = password + salt
    # Hash using SHA-256
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
    return hashed_password

def verify_password(password, hashed_password, salt=""):
    # Re-hash the input password and compare
    return hash_password(password, salt) == hashed_password