def save():
    rollno=t1.get()
    name=t2.get()
    sql="insert into student values(%s,%s)"
    data=(rollno,name)
    s1.execute(sql,data)
    db.commit()
    messagebox.showinfo("Success","Data Saved")

import mysql.connector
from tkinter import *
from tkinter import messagebox
db=mysql.connector.connect(host="localhost",user="root",password="manager",database="veer")
s1=db.cursor()

win=Tk()
win.state('zoomed')

l1=Label(text="Enter Roll no",font=('tahoma',20,'bold'))
l2=Label(text="Enter Name",font=('tahoma',20,'bold'))
t1=Entry(font=('tahoma',20,'bold'))
t2=Entry(font=('tahoma',20,'bold'))

b1=Button(text="Save",font=('tahoma',20,'bold'),command=save)

l1.grid(row=0,column=1,padx=40,pady=40)
t1.grid(row=0,column=2)
l2.grid(row=1,column=1,padx=40,pady=40)
t2.grid(row=1,column=2)
b1.grid(row=2,column=2,padx=40,pady=40)


win.mainloop()
