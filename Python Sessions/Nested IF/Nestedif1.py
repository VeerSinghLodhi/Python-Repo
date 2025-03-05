
username=input("Enter your username : ")

if username=="admin":
    password = input("Enter your password : ")
    if password=="12345":
        print("You can login")
    else:
        print("Wrong password")
else:
    print("Wrong username")
