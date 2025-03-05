
price=int(input("Enter price : "))
qty=int(input("Enter quantity : "))
total=price*qty
if price<0 or qty<0:
    print("Please enter valid price or quantity")
else:
    if total>=0 and total<500:
        dis=0
    elif total>=500 and total<1000:
        dis=total*3/100
    elif total>=1000 and total<1500:
        dis=total*5/100
    elif total>=1500:
        dis=total*10/100
    net=total-dis
    print("Total ",total)
    print("Discount ",dis)
    print("Net ",net)
