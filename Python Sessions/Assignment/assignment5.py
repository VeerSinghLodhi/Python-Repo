
classesHeld=int(input("Enter the number of classes held : "))
classesAttended=int(input("Enter the number of classes attended : "))

percentage=(classesAttended/classesHeld)*100
print("Percentage of classes attended : ",percentage,"%")
if percentage>=75:
    print("The student is allowed to sit in the exam.")
else:
    print("The student is not allowed to sit in the exam.")
