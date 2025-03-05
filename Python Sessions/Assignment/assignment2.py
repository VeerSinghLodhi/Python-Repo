
salary=float(input("Enter the salary : "))
year=int(input("Enter the year : "))

if year>5:
    dis=salary*5/100
else:
    dis=0
salary+=dis
print("Salary is ",salary)
print("Year is ",year)

