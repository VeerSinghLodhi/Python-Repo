

num=int(input("Enter a number : "))

if num%2==0:
    print("Even")
    if num%5==0:
        print("Divisible by 5")
    else:
        print("Not divisible by 5")
else:
    print("Odd")