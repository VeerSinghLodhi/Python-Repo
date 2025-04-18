def check():
    ans=combo.get() # get Values like getSelectedItem() in java
    print(ans)
    i=combo.current()   # get index like getSeletedIndex() in java
    print(i)
    if i==0:
        l2.config(text=ans+'language, 3 Months')
    elif i==1:
        l2.config(text='4 Months')
    elif i==2:
        l2.config(text='5 Months')
    elif i==3:
        l2.config(text='6 Months')


from tkinter import *
from tkinter import ttk

win=Tk()
win.state('zoomed')

l1=Label(text='Select a language',font=('tahoma',20,'bold'))
lang=('C','C++','Java','Python','Java-Script')
combo=ttk.Combobox(values=lang,font=('tahoma',20,'bold'))
l2=Label(font=('tahoma',20,'bold'))
b1=Button(text='OK',font=('tahoma',20,'bold'),command=check)

l1.pack()
combo.pack()
b1.pack()
l2.pack()
win.mainloop()
