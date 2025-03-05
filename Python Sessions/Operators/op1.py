
import random
num1=random.randint(1,10)
num2=int(input("Enter a number between 1 and 10 : "))
i=0
while num1!=num2:
    num1 = random.randint(1, 10)
    num2=int(input("Again Enter a number between 1 and 10 : "))
    i+=1

print("After ",i)
print(num1," ",num2)