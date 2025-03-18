numbers=[]
for i in range(10):
    print("Enter ",i+1," number : ",end="")
    num=int(input())
    numbers.append(num)
print('Normal List')
print(numbers)
print('---------------------------------------------')
odd_numbers=[]
for i in numbers:
    if i%2==0:
        odd_numbers.append(i)
print('Odd numbers list')
print(odd_numbers)