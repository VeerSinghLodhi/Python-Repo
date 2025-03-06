
age=int(input("Enter your age : "))
license=input("Do you have a driver's license?(Yes/No): ")

if age>16:
    if license=="Yes":
        print("You are eligible for a learner's permit.")
    elif license=="No":
        print("You are not eligible for a learner's permit.")
    else:
        print("Invalid license")
else:
    print("You are not eligible for a learner's permit.")