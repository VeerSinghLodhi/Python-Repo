
num=int(input("Enter a Number : "))
temp=num
reversed=0
while num!=0:
    reversed=(reversed*10)+num%10
    num//=10
if reversed==temp:
    print(temp," is a Palindrome number.")
else:
    print(temp," is not a Palindrome number.")