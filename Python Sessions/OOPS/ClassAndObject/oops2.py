class Employee:  # Class
    def setEmployee(self,emp_id,name,salary): # Setter
        self.emp_id=emp_id
        self.name=name
        self.salary=salary
    def getEmployee(self): # Getter
        print('Employee id : ',self.emp_id)
        print('Name : ',self.name)
        print('Salary : ',self.salary)

e1=Employee()   # Object
empid=int(input("Enter Employee id : "))
name=input("Enter name : ")
salary=int(input("Enter Salary"))
e1.setEmployee(empid,name,salary)
e1.getEmployee()