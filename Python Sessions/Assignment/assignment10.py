'''
Write a program that takes a value from the user and prints reverse counting
from that no. to 1.
Example :
Enter a number : 20
Output : 20,19,18…..1
If the entered number is a negative value, print reverse counting from 10 to 1
Example :
Enter a number : -30
Output : 10,9,8…..1
'''
num=int(input("Enter a value : "))
if num<0:
    num=10
for i in range(num,0,-1):
    print(i,",",end=" ")