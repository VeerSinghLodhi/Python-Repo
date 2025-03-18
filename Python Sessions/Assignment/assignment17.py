my_list=[2,4,6,8,10]

# List Length
length=len(my_list)
print('Length of list is ',length)

# First Element of the list
print(my_list[0])

# Last Element of the list
print(my_list[-1])
# OR
print(my_list[length-1])

# Sum of the all Elements
sum=0
for i in my_list:
    sum+=i
print('Sum of the all elements in list is ',sum)

# Append the new number 12 at the end of the list
my_list.append(12)
print(my_list)

# Insert the new number 0 at the Beginning of the list
my_list.insert(0,0)
print(my_list)

# Remove the number 6 from the list
my_list.remove(6)
print(my_list)

# Sort the list in descending order
my_list.sort(reverse=True)
print(my_list)

# Check if the number 5 is in the list
c=my_list.count(5)
print(c)

# Doubled List
doubled_list=[]
for i in my_list:
    doubled_list.append(i*2)
doubled_list.sort()
print(doubled_list)