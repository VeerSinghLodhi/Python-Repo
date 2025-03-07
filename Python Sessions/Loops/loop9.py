'''
    *****
     ****
       ***
         **
           *
Draw this pattern
'''
#Answer
for i in range(6,1,-1):
    for j in range(6,1,-1):
        if i>=j:
            print("*",end=" ")
        else:
            print("  ",end=" ")
    print()