ch=1
while ch!=3:
    print("1. Option one")
    print("2. Option two")
    print("3. Exit")
    print("-------------------------------------------")
    ch=int(input("Select an Option : "))
    if ch==1:
        print("Option one")
    elif ch==2:
        print("Option two")
    elif ch==3:
        print("Exited")
    else:
        print("Invalid Option")
    print("-------------------------------------------")
