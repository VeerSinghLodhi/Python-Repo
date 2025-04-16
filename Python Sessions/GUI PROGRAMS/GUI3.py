
def checkUser():
    try:
        uname=userTextField.get()
        upass=passTextField.get()
        if uname=='Admin':
            if upass=='veerhani':
                show.config(fg='blue')
                show.config(text="You Can Login")
            else:
                show.config(fg='red')
                show.config(text="Invalid password!!")
        else:
            show.config(fg='red')
            show.config(text="Invalid Username")
    except:
        show.config("Error!!")
            
def clear():
    userTextField.delete(0,END)
    passTextField.delete(0,END)
    show.config(text="")
    userTextField.focus()

from tkinter import *
win=Tk()
win.state('zoomed')

l1=Label(text="Login Window",font=('tahoma',30,'bold'))

username=Label(text="Enter Your User",font=('tahoma',20,'bold'))
password=Label(text="Enter Your Password",font=('tahoma',20,'bold'))
show=Label(font=('tahoma',20,'bold'))

userTextField=Entry(font=('tahoma',20,'bold'))
passTextField=Entry(font=('tahoma',20,'bold'))

btn1=Button(text="Login",font=('tahoma',20,'bold'),command=checkUser)
btn2=Button(text="Reset",font=('tahoma',20,'bold'),command=clear)

l1.pack()
username.pack()
userTextField.pack()
password.pack()
passTextField.pack()
btn1.pack()
btn2.pack()
show.pack()

win.config(bg="red")
win.title("Welcome to veer application")
win.mainloop()