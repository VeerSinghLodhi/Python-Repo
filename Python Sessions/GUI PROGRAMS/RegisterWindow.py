def savedata():
        rollno=t1.get()
        name=t2.get()
        username=t3.get()
        password=t4.get()
        cpassword=t5.get()
        if password!=cpassword:
                messagebox.showerror("Error","Passwords do not match")
        else:
            sql="insert into register values(%s,%s,%s,%s)"
            # data=(ro)
def reset():
        print('veer')


import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
con=mysql.connector.connect(host="localhost",user="root",password="manager",database="veer")
cursor=con.cursor()

win=Tk()
win.title("Registration Window")
win.resizable(width=False,height=False)
win.state("zoomed")

l1=ttk.Label(win,text="Roll No.",font=("tahoma",20,"bold"))
l2=ttk.Label(win,text="Name",font=("tahoma",20,"bold"))
l3=ttk.Label(win,text="Username",font=("tahoma",20,"bold"))
l4=ttk.Label(win,text="Password",font=("tahoma",20,"bold"))
l5=ttk.Label(win,text="Confirm password",font=("tahoma",20,"bold"))

t1=ttk.Entry(win,font=("tahoma",20,"bold"))
t2=ttk.Entry(win,font=("tahoma",20,"bold"))
t3=ttk.Entry(win,font=("tahoma",20,"bold"))
t4=ttk.Entry(win,font=("tahoma",20,"bold"))
t5=ttk.Entry(win,font=("tahoma",20,"bold"))

b1=ttk.Button(win,text="Register",command=savedata)
b2=ttk.Button(win,text="Reset",command=reset)
b3=ttk.Button(win,text="Login")

l1.place(x=100,y=100)
t1.place(x=400,y=100)
l2.place(x=100,y=200)
t2.place(x=400,y=200)
l3.place(x=100,y=300)
t3.place(x=400,y=300)
l4.place(x=100,y=400)
t4.place(x=400,y=400)
l5.place(x=100,y=500)
t5.place(x=400,y=500)

b1.place(x=400,y=600,width=150,height=40)
b2.place(x=600,y=600,width=150,height=40)
b3.place(x=400,y=650,width=350,height=40)
win.mainloop()