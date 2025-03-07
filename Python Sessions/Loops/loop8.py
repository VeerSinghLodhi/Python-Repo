'''
*****
****
***
**
*
Draw this pattern
'''
#Answer
for i in range(5,0,-1):
    for j in range(1,6,1):
        if j<=i:
            print("*",end=" ")
        else:
            print(end=" ")
    print()