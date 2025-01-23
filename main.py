from hasher import hash_password, verify_password

def main():
    print("Welcome to the Password Hasher!")
    password = input("Enter a password to hash: ")
    salt = input("Enter a salt (optional): ")

    # Hash the password
    hashed = hash_password(password, salt)
    print(f"Hashed password: {hashed}")

    # Verify the password
    verify = input("Enter the password again to verify: ")
    if verify_password(verify, hashed, salt):
        print("Password verified!")
    else:
        print("Password does not match!")

if __name__ == "__main__":
    main()