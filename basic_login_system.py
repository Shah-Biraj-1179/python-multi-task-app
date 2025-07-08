# Basic Login System

def login():
    print("Basic Login System")
    stored_username = "admin"
    stored_password = "password123"

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == stored_username and password == stored_password:
        print("Login successful!")
    else:
        print("Login failed. Invalid credentials.")

if __name__ == "__main__":
    login()
