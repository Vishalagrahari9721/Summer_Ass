#Program to keep asking password until correct
correct_password = "python123"
password = ""

while password != correct_password:
    password = input("Enter password:")

    print("Access Granted!")