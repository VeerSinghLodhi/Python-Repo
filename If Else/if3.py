
product_price=float(input("Enter Product Price : "))
quantity=float(input("Enter Quantity : "))
total=product_price*quantity
dis=0
if total>=1000 :
    dis=total*5/100

net=total-dis
print("Total price is ",total)
print("Discount is ",dis)
print("Net Price is ",net)