'''
Write a program to get ‘age’ and ‘gender’ of 10 people. Print no. of males,
females and their avg. age
Example :
Enter Gender : M
Enter Age : 20
Enter Gender : F
Enter Age : 24
Enter Gender : M
Enter Age : 30
Enter Gender : F
Enter Age : 12
No. of males : 2
No. of females : 2
Avg. male age : 25
Avg. female age : 18
'''
male=female=mage=fage=others=0
for i in range(1,11,1):
    ch=input("Enter Gender : ")
    age=int(input("Enter Age : "))
    if ch=="M" or ch=="m":
        male+=1
        mage+=age
    elif ch=="F" or ch=="f":
        female+=1
        fage+=age
    else:
        others+=1
print("No. of males : ",male)
print("No. of females : ",female)
if male>0:
    maleAvg=mage/male
    print("Avg. male age : ",maleAvg)
if female>0:
    femaleAvg=fage/female
    print("Avg. female age : ",femaleAvg)
print("No. of others : ",others)


