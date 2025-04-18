
def getAns():
    if len(t1.get())==0:
        messbox=messagebox.showerror('Error','Enter a value')
        return
    num=int(t1.get())
    if num<1:
        messbox=messagebox.showwarning('Negative value!','You entered negative value')
    
    sq=num*num
    messagebox.showinfo('Square','Square is '+str(sq))


def close():
    ans=messagebox.askyesno('Confirmation?','Do you want to close this program?')
    if ans:
        top.destroy()

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
top=Tk()
top.state('zoomed')


l1=ttk.Label(text='Enter a number')
t1=ttk.Entry()
b1=ttk.Button(text='OK',command=getAns)
b2=ttk.Button(text='Close',command=close)


l1.pack()
t1.pack()
b1.pack()
b2.pack()



top.mainloop()