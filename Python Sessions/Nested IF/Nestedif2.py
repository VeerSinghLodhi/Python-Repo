
number=int(input("Enter a number : "))

if number%2==0:
    print("The number is even")
    if number%5==0:
        print("The number is divisible by 5")
    else:
        print("But the number is not divisible by 5")
else:
    print("The number is odd")
    if  number%5==0:
        print("The number is divisible by 5")
    else:
        print("But the number is not divisible by 5")