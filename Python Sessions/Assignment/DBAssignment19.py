def savedata():
    drname=t1.get()
    v=var1.get()
    if v==1:
        sex="Male"
    else:
        sex="Female"
    department=cb1.get()
    consultationday=cb2.get()
    ctime1=t2.get()
    ctime2=t3.get()
    address=ta1.get("1.0",END)
    contact_no=t4.get()
    emergency_no=t5.get()
    consultation_fee=t6.get()
    total_patients=t7.get()
    date=t8.get()
    if len(drname)==0 or len(sex)==0 or len(department)==0 or len(consultationday)==0 or len(ctime1)==0 or len(ctime2)==0 or len(address)==0 or len(contact_no)==0 or len(emergency_no)==0 or len(consultation_fee)==0 or len(total_patients)==0 or len(date)==0:
        messagebox.showerror("Error","Fill all the fields")
        return;
    data=(drname,sex,department,consultationday,ctime1,ctime2,address,contact_no,emergency_no,consultation_fee,total_patients,date)
    sql="insert into doctors values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    print(data)
    c1.execute(sql,data)
    db.commit()
    messagebox.showinfo("Success","Registration Successful")

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",password="manager",database="veer")
c1=db.cursor()

win=Tk()
win.state('zoomed')

title=Label(text="DOCTOR'S REGISTRATION",font=("tahoma",25,"bold"))
l1=Label(text="Doctor Name",font=("tahoma",18,"bold"))
l2=Label(text="Sex",font=("tahoma",18,"bold"))
l3=Label(text="Department",font=("tahoma",18,"bold"))
l4=Label(text="Consultation Day",font=("tahoma",18,"bold"))
l5=Label(text="Consultation Time",font=("tahoma",18,"bold"))
l6=Label(text="Address",font=("tahoma",18,"bold"))
l7=Label(text="Contact Number",font=("tahoma",18,"bold"))
l8=Label(text="Emergency Number",font=("tahoma",18,"bold"))
l9=Label(text="Consultation Fee",font=("tahoma",18,"bold"))
l10=Label(text="Total Patients",font=("tahoma",18,"bold"))
l11=Label(text="Date",font=("tahoma",18,"bold"))
l12=Label(text="Example[10:30am]",font=("tahoma",12,"normal"))
l13=Label(text="Example[1:30pm]",font=("tahoma",12,"normal"))
l14=Label(text="From",font=("tahoma",12,"normal"))
l15=Label(text="To",font=("tahoma",12,"normal"))

t1=Entry(font=("tahoma",18,"bold"))
t2=Entry(font=("tahoma",18,"bold"))
t3=Entry(font=("tahoma",18,"bold"))
t4=Entry(font=("tahoma",18,"bold"))
t5=Entry(font=("tahoma",18,"bold"))
t6=Entry(font=("tahoma",18,"bold"))
t7=Entry(font=("tahoma",18,"bold"))
t8=Entry(font=("tahoma",18,"bold"))


ta1=Text(font=("tahoma",18,"bold"),width=21,height=2)

var1=IntVar()
r1=Radiobutton(text="Male",variable=var1,value=1,font=("tahoma",18,"bold"))
r2=Radiobutton(text="Female",variable=var1,value=2,font=("tahoma",18,"bold"))


data=["General Medicine","Family Medicine","Emergency Medicine","Community Medicine","Geriatric Medicine","Infectious Diseases","Hospital Medicine"]
cb1=Combobox(win,values=data,font=("tahoma",18,"bold"))
data=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
cb2=Combobox(win,values=data,font=("tahoma",18,"bold"))


b1=Button(text="Save",font=("tahoma",15,"bold"),command=savedata)
b2=Button(text="Cancel",font=("tahoma",15,"bold"),command=win.destroy)

title.place(x=500,y=20)
l1.place(x=300,y=100)
t1.place(x=600,y=100)

l2.place(x=300,y=150)
r1.place(x=600,y=150)
r2.place(x=700,y=150)

l3.place(x=300,y=200)
cb1.place(x=600,y=200)

l4.place(x=300,y=250)
cb2.place(x=600,y=250)

l5.place(x=300,y=330)
t2.place(x=600,y=330,width=80)
t3.place(x=800,y=330,width=80)
l12.place(x=600,y=300)
l13.place(x=800,y=300)
l14.place(x=550,y=330)
l15.place(x=750,y=330)

l6.place(x=300,y=380)
ta1.place(x=600,y=380)

l7.place(x=300,y=450)
t4.place(x=600,y=450)

l8.place(x=300,y=500)
t5.place(x=600,y=500)

l9.place(x=300,y=550)
t6.place(x=600,y=550)

l10.place(x=300,y=600)
t7.place(x=600,y=600)

l11.place(x=300,y=650)
t8.place(x=600,y=650)

b1.place(x=600,y=700)
b2.place(x=800,y=700)

win.mainloop()