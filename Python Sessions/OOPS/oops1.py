class Student:
    def setStudent(self,rollno,name):
        self.rollno=rollno
        self.name=name;
    def getStudent(self):
        print('Roll no : ',self.rollno)
        print('Name : ',self.name)

s1=Student()
rollno=int(input("Enter roll no : "))
name=input("Enter name : ")
s1.setStudent(rollno,name)
s1.getStudent()