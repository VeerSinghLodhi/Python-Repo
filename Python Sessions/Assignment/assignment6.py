
classesHeld=int(input("Enter the number of classes held : "))
classesAttended=int(input("Enter the number of classes attended : "))
medicalCause=input("Do you have medical cause? (Y/N) : ")
percentage=(classesAttended/classesHeld)*100
print("-----------------------------------------------------------------")
print("Percentage of classes attended : ",percentage,"%")
print("Do you have medical cause? (Y/N) : ",medicalCause)

if percentage>=75 or medicalCause=="Y" or medicalCause=="y":
    print("The student is allowed to sit in the exam.")
else:
    print("The student is not allowed to sit in the exam.")
