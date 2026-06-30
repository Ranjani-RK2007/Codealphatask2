import hashlib

MAX_ATTEMPTS = 3

stored_username = "admin"

stored_password = hashlib.sha256("Admin@123".encode()).hexdigest()

attempt = 0

while attempt < MAX_ATTEMPTS:
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if username == stored_username and hashed_password == stored_password:
        print("Login Successful")
        break
    else:
        attempt += 1
        print("Invalid Username or Password")

if attempt == MAX_ATTEMPTS:
    print("Account Locked. Too many failed attempts.")
