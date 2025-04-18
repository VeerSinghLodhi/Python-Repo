
def close():
    win.destroy()

def createwindow():
    top=Toplevel()
    top.title('New File')
    top.mainloop()

from tkinter import *
from tkinter import ttk

win=Tk()
win.state('zoomed')

pic=PhotoImage(file='C:/Users/Veersingh Lodhi/Downloads/pngwing.com (1).png')
l1=Label(image=pic)
#l1.pack()


menubar=Menu()


filemenu=Menu(tearoff=0)
filemenu.add_command(label='Open',command=createwindow)
filemenu.add_command(label='Save')
filemenu.add_command(label='Exit',command=close)

menubar.add_cascade(menu=filemenu, label='File')
menubar.add_cascade(label='Edit')
menubar.add_cascade(label='View')
menubar.add_cascade(label='Exit',command=close)



win.config(menu=menubar)




win.mainloop()