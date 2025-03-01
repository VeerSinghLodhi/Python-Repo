
cost_price=float(input("Enter Cost Price : "))
selling_price=float(input("Enter Selling Price : "))

if selling_price>cost_price:
    print("Profit is ",selling_price-cost_price)
elif selling_price<cost_price:
    print("Loss is",cost_price-selling_price)
else:
    print("No Profit , No Loss")