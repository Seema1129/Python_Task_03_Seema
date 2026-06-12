# Password Attempt Simulator

password = "seema123"
attempts = 3

while attempts > 0:
    user_password = input("Enter password: ")

    if user_password == password:
        print("Access Granted")
        break
    else:
        attempts -= 1
        print("Incorrect Password")
        print("Attempts Left:", attempts)

if attempts == 0:
    print("Account Locked")