'''
Can you write a for loop that generates a sequence of numbers with a custom
step size (not just 1)? For example, print numbers from 1 to 10 with a step size of 2.
'''
num=int(input("Enter a number : "))
for i in range(1,num+1,2):
    print(i,end=" ")