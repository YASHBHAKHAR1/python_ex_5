def main():

    correct_username = "prince"
    correct_password = "prince@121"
    attempts = 0
    max_attempts = 5
    while attempts < max_attempts:

        username = input("Enter your username: ")
        password = input("Enter your password: ")


        if username == correct_username and password == correct_password:
            print("Welcome!")
            return
        else:
            print("Incorrect username or password.")
            attempts += 1


    print("Access denied.")

if __name__ == "__main__":
    main()
