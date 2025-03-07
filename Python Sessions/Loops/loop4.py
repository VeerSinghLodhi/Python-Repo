
c=java=python=js=others=0
for i in range(1,11,1):
    print("C for C Language")
    print("J for Java Language")
    print("P for Python Language")
    print("JS for Java Script Language")
    ch=input("Select a choice : ")
    print("-------------------------------------------------")
    if ch=='C' or ch=='c':
        c+=1
    elif ch=='J' or ch=='j':
        java+=1
    elif ch=='P' or ch=='p':
        python+=1
    elif ch=='JS' or ch=='js' or ch=='jS' or ch=='Js':
        js+=1
    else:
        others+=1
print("C language is ",c)
print("Java language is ",java)
print("Python language is ",python)
print("Java Script language is ",js)
print("Others is ",others)