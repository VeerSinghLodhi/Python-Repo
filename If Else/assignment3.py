
quantity=int(input("Enter the Quantity of items : "))
total=quantity*100

if total>1000:
    dis=total*10/100
else:
    dis=0
net=total-dis
print("Quantity of items :",quantity)
print("Total : ",total)
print("Discount :" ,dis)
print("Net : ",net)