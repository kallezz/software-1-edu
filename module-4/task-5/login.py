correct_user = "python"
correct_pass = "rules"
attempts = 4

while True:
    user = input("Enter username: ")
    passwd = input("Enter password: ")

    if (user == correct_user) and (passwd == correct_pass):
        print("Welcome")
        break
    elif attempts == 0:
        print("Access denied")
        break
    else:
        print("Incorrect username or password. Please try again.")
        attempts -= 1
        continue
