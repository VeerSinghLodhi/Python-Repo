
marks=int(input("Enter the number of marks : "))
if marks<25 and marks>0:
    print("Your Grade is F")
elif marks>=25 and marks<45:
    print("Your Grade is E")
elif marks>=45 and marks<50:
    print("Your Grade is D")
elif marks>=50 and marks<60:
    print("Your Grade is C")
elif marks>=60 and marks<80:
    print("Your Grade is B")
elif marks>=80 and marks<=100:
    print("Your Grade is A")
else:
    print("Invalid marks")