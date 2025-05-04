
import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
db=mysql.connector.connect(host="localhost",user="root",password="manager",database="companydb")
cursor=db.cursor()

def get_emp_id():
    sql="select  max(emp_id) from employees";
    cursor.execute(sql)
    id=cursor.fetchone()
    if id[0]==None:
        emp_id=101
    else:
        emp_id=id[0]+1
    print(emp_id)
    return emp_id

def add_employees():
    '''----Add New Employee----'''
    top=Toplevel()
    top.title("Add Employees")
    top.resizable(width=False,height=False)
    top.geometry("700x450")
    emp_title = Label(top, text="Add New Employee", font=("tahoma", 26, "italic"))
    emp_name_label=Label(top,text="Employee Name",font=("arial",16,"bold"))
    emp_department_label=Label(top,text="Department",font=("arial",16,"bold"))
    emp_salary_label=Label(top,text="Employee Salary",font=("arial",16,"bold"))

    emp_name_entry=Entry(top,font=("arial",16,"bold"))
    emp_salary_entry=Entry(top,font=("arial",16,"bold"))

    data=("Human Resources","Finance and Accounting","Marketing","Sales","Operations")
    department_list=Combobox(top,values=data,font=("arial",16,"bold"))
    def reset():
        emp_name_entry.delete(0,END)
        emp_salary_entry.delete(0,END)
        department_list.delete(0,END)
        emp_name_entry.focus()

    def addemp():
        id=get_emp_id()
        name=emp_name_entry.get()
        department=department_list.get()
        salary=emp_salary_entry.get()
        data=(id,name,department,salary)
        sql="insert into employees values(%s,%s,%s,%s)"
        cursor.execute(sql,data)
        db.commit()
        messagebox.showinfo("Employee added","Employee Added Successfully")
        top.destroy()

    save_button=Button(top,text="Save",font=("arial",16,"bold"),command=addemp)
    reset_button=Button(top,text="Reset",font=("arial",16,"bold"),command=reset)
    cancel_button=Button(top,text="Cancel",font=("arial",16,"bold"),command=top.destroy)


    emp_title.place(x=180,y=20)

    emp_name_label.place(x=50,y=100)
    emp_name_entry.place(x=250, y=100,width=300)

    emp_department_label.place(x=50,y=160)
    department_list.place(x=250,y=160,width=300)

    emp_salary_label.place(x=50,y=220)
    emp_salary_entry.place(x=250,y=220,width=300)

    save_button.place(x=50,y=350,width=160,height=40)
    reset_button.place(x=280,y=350,width=160,height=40)
    cancel_button.place(x=480,y=350,width=160,height=40)
    top.mainloop()

def show_employees():
   '''---- Show All Employees----'''
   top = Toplevel()
   top.title("Show All Employees")
   top.resizable(width=False, height=False)
   top.geometry("700x450")
   emp_title = Label(top, text="Show All Employees", font=("tahoma", 26, "italic"))
   select_id_label = Label(top, text="Select a Employee ID", font=("arial", 16, "bold"))
   emp_name_label= Label(top, text="Employee Name", font=("arial", 16, "bold"))
   emp_department_label = Label(top, text="Employee Department", font=("arial", 16, "bold"))
   emp_salary_label = Label(top, text="Employee Salary", font=("arial", 16, "bold"))

   show_emp_name_label = Label(top, text="Select a ID", font=("arial", 16, "bold"))
   show_emp_department_label = Label(top, text="Select a ID", font=("arial", 16, "bold"))
   show_emp_salary_label = Label(top, text="Select a ID", font=("arial", 16, "bold"))

   def reset():
       show_emp_name_label.configure(text="Select a ID")
       show_emp_department_label.configure(text="Select a ID")
       show_emp_salary_label.configure(text="Select a ID")
       emp_id_list.delete(0, END)
   def show_details():
            emp_id=emp_id_list.get()
            sql="select emp_name,department,salary from employees where emp_id=%s"
            data=(emp_id,)
            cursor.execute(sql,data)
            records=cursor.fetchone()
            show_emp_name_label.configure(text=records[0])
            show_emp_department_label.configure(text=records[1])
            show_emp_salary_label.configure(text=records[2])


   show_button = Button(top, text="Show", font=("arial", 16, "bold"), command=show_details)
   reset_button = Button(top, text="Reset", font=("arial", 16, "bold"),command=reset)
   cancel_button = Button(top, text="Cancel", font=("arial", 16, "bold"), command=top.destroy)

   sql="select emp_id from employees";
   cursor.execute(sql)
   res=cursor.fetchall()
   emp_id_list = Combobox(top, values=res, font=("arial", 16, "bold"))


   emp_title.place(x=180, y=20)
   select_id_label.place(x=50, y=100)
   emp_id_list.place(x=320, y=100,width=300)

   emp_name_label.place(x=50,y=160)
   show_emp_name_label.place(x=320,y=160)

   emp_department_label.place(x=50,y=220)
   show_emp_department_label.place(x=320,y=220)

   emp_salary_label.place(x=50,y=280)
   show_emp_salary_label.place(x=320,y=280)

   show_button.place(x=50, y=350, width=160, height=40)
   reset_button.place(x=280, y=350, width=160, height=40)
   cancel_button.place(x=480, y=350, width=160, height=40)

def update_employees():
        '''---Update Employees---'''
        top = Toplevel()
        top.title("Update All Employees")
        top.resizable(width=False, height=False)
        top.geometry("700x450")
        emp_title = Label(top, text="Update Employees", font=("tahoma", 26, "italic"))
        select_id_label = Label(top, text="Select a Employee ID", font=("arial", 16, "bold"))
        emp_name_label = Label(top, text="Employee Name", font=("arial", 16, "bold"))
        emp_department_label = Label(top, text="Employee Department", font=("arial", 16, "bold"))
        emp_salary_label = Label(top, text="Employee Salary", font=("arial", 16, "bold"))

        emp_name_var = StringVar()
        emp_salary_var = StringVar()
        emp_name_entry = Entry(top, font=("arial", 16, "bold"),textvariable=emp_name_var)
        emp_salary_entry = Entry(top, font=("arial", 16, "bold"),textvariable=emp_salary_var)

        data = ("Human Resources", "Finance and Accounting", "Marketing", "Sales", "Operations")
        department_list = Combobox(top, values=data, font=("arial", 16, "bold"))


        def reset():
            emp_name_entry.delete(0,END)
            department_list.delete(0,END)
            emp_salary_entry.delete(0,END)
            emp_id_list.delete(0, END)
            emp_id_list.focus()

        def show_details():
            print("Hello")
            emp_id = emp_id_list.get()
            sql = "select emp_name,department,salary from employees where emp_id=%s"
            data = (emp_id,)
            cursor.execute(sql, data)
            records = cursor.fetchone()
            emp_name_var.set(records[0])
            department_list.set(records[1])
            emp_salary_var.set(records[2])
        def record_update():
            print("Record Updated")
            id=emp_id_list.get()
            name=emp_name_entry.get()
            department=department_list.get()
            salary=emp_salary_entry.get()
            sql="update employees set emp_name=%s,department=%s,salary=%s where emp_id=%s"
            data=(name,department,salary,id)
            cursor.execute(sql, data)
            db.commit()
            messagebox.showinfo("Success", "Record Updated")
            reset()

        show=Button(top, text="Show", font=("arial", 12, "bold"), command=show_details)
        show_button = Button(top, text="Update", font=("arial", 16, "bold"),command=record_update)
        reset_button = Button(top, text="Reset", font=("arial", 16, "bold"), command=reset)
        cancel_button = Button(top, text="Cancel", font=("arial", 16, "bold"), command=top.destroy)

        sql = "select emp_id from employees";
        cursor.execute(sql)
        res = cursor.fetchall()
        emp_id_list = Combobox(top, values=res, font=("arial", 16, "bold"))

        emp_title.place(x=180, y=20)
        select_id_label.place(x=50, y=100)
        emp_id_list.place(x=320, y=100, width=300)
        show.place(x=630, y=100, width=50, height=30)

        emp_name_label.place(x=50, y=160)
        emp_name_entry.place(x=320, y=160, width=300)

        emp_department_label.place(x=50, y=220)
        department_list.place(x=320, y=220, width=300)

        emp_salary_label.place(x=50, y=280)
        emp_salary_entry.place(x=320, y=280, width=300)

        show_button.place(x=50, y=350, width=160, height=40)
        reset_button.place(x=280, y=350, width=160, height=40)
        cancel_button.place(x=480, y=350, width=160, height=40)


def delete_employees():
    '''---Delete Employees---'''
    top = Toplevel()
    top.title("Delete Employees")
    top.resizable(width=False, height=False)
    top.geometry("700x450")
    emp_title = Label(top, text="Delete Employees", font=("tahoma", 26, "italic"))
    select_id_label = Label(top, text="Select a Employee ID", font=("arial", 16, "bold"))
    emp_name_label = Label(top, text="Employee Name", font=("arial", 16, "bold"))
    emp_department_label = Label(top, text="Employee Department", font=("arial", 16, "bold"))
    emp_salary_label = Label(top, text="Employee Salary", font=("arial", 16, "bold"))

    show_emp_name_label = Label(top, text="Select a ID", font=("arial", 16, "bold"))
    show_emp_department_label = Label(top, text="Select a ID", font=("arial", 16, "bold"))
    show_emp_salary_label = Label(top, text="Select a ID", font=("arial", 16, "bold"))

    def reset():
        show_emp_name_label.configure(text="Select a ID")
        show_emp_department_label.configure(text="Select a ID")
        show_emp_salary_label.configure(text="Select a ID")
        emp_id_list.delete(0, END)

    def show_details():
        emp_id = emp_id_list.get()
        sql = "select emp_name,department,salary from employees where emp_id=%s"
        data = (emp_id,)
        cursor.execute(sql, data)
        records = cursor.fetchone()
        show_emp_name_label.configure(text=records[0])
        show_emp_department_label.configure(text=records[1])
        show_emp_salary_label.configure(text=records[2])

    def record_delete():
        print("Record Delete")
        id=emp_id_list.get()
        sql="delete from employees where emp_id=%s"
        data=(id,)
        cursor.execute(sql, data)
        messagebox.showinfo("Success", "Record Deleted")
        reset()
        reload_id()

    show = Button(top, text="Show", font=("arial", 12, "bold"), command=show_details)
    show_button = Button(top, text="Delete", font=("arial", 16, "bold"), command=record_delete)
    reset_button = Button(top, text="Reset", font=("arial", 16, "bold"), command=reset)
    cancel_button = Button(top, text="Cancel", font=("arial", 16, "bold"), command=top.destroy)

    sql = "select emp_id from employees";
    cursor.execute(sql)
    res = cursor.fetchall()
    emp_id_list = Combobox(top, values=res, font=("arial", 16, "bold"))
    def reload_id():
        sql = "select emp_id from employees";
        cursor.execute(sql)
        res = cursor.fetchall()
        emp_id_list.config(values=res)

    emp_title.place(x=180, y=20)
    select_id_label.place(x=50, y=100)
    emp_id_list.place(x=320, y=100, width=300)
    show.place(x=630, y=100, width=50, height=30)

    emp_name_label.place(x=50, y=160)
    show_emp_name_label.place(x=320, y=160)

    emp_department_label.place(x=50, y=220)
    show_emp_department_label.place(x=320, y=220)

    emp_salary_label.place(x=50, y=280)
    show_emp_salary_label.place(x=320, y=280)

    show_button.place(x=50, y=350, width=160, height=40)
    reset_button.place(x=280, y=350, width=160, height=40)
    cancel_button.place(x=480, y=350, width=160, height=40)

get_emp_id()
win=Tk()
win.state('zoomed')

menubar=Menu(font=("arial",20,"bold"))
filemenu=Menu(tearoff=0)
editmenu=Menu()
filemenu.add_command(label="Add New Employee", font=("arial",13,"normal"),command=add_employees)
filemenu.add_command(label="Show All Employees",font=("arial",13,"normal"), command=show_employees)
filemenu.add_command(label="Update Employees",font=("arial",13,"normal"), command=update_employees)
filemenu.add_command(label="Delete Employee",font=("arial",13,"normal"), command=delete_employees)
filemenu.add_separator()
filemenu.add_command(label="Exit",font=("arial",13,"normal"), command=win.destroy)

menubar.add_cascade(label="Employee",font=("Arial",20,"bold"), menu=filemenu)

win.config(menu=menubar)
win.mainloop()

