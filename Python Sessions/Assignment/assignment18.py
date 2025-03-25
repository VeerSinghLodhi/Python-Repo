# SET ASSIGNMENT
groupA={"Hiking","Swimming","Reading","Cooking","Painting"}
groupB={"Gaming","Cooking","Hiking","Photography","Dancing"}

print("Group A : \n",groupA)
print("Group B : \n",groupB)
print('-----------------------------------------------------------------------------')
# Union- favourite activities
print('Combined favourite activities')
print(groupA|groupB)
# OR
print(groupA.union(groupB))

#Intersection Comman Activities
print('Activities that are common')
print(groupA & groupB)
# OR
print(groupA.intersection(groupB))

# Symmentic difference Unique Activities
print('activities that are unique')
print(groupA ^ groupB)
# OR
print(groupA.symmetric_difference(groupB))

# Difference GroupA - GroupB
print(groupA - groupB)
# OR
print(groupA.difference(groupB))

activity='Swimming'
if activity in groupA and activity in groupB:
    print( activity,' is common in groupA and groupB')
elif activity in groupA:
    print( activity,' is common in groupA')
elif activity in groupB:
    print( activity,' is common in groupB')
else:
    print(activity,'Doesn\'t exist in groupA and groupB')


