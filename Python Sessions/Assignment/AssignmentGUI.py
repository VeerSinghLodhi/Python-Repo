def showCost():
    name=lis.get(ANCHOR)
    if name=='Monthly':
        price=300
    elif name=='Quarterly':
        price=900
    elif name=='Half-Yearly':
        price=1500
    elif name=='Yearly':
        price=3500
    else:
        l1.config(text='Please Select a Plain',fg='red')
        return 0
    l1.config(text=price,fg='blue')
    return price


def getcal():
    price=showCost()
    if price==0:
        l1.config(text='Please Select a Plain')
        return
    if len(t1.get())==0:
        l2.config(fg='red')
        return
    l2.config(fg='black')
    noofmember=int(t1.get())
    total=price*noofmember
    isStudent=t2.get()
    if isStudent=='y' or isStudent=='y' or isStudent=='yes' or isStudent=='YES':
        dis=total*15/100
    else:
        dis=0
    net=total-dis
    l5.config(text=total)
    l7.config(text=dis)
    l9.config(text=net)
    
def clear():
    t1.delete(0,END)
    t2.delete(0,END)
    l1.config(text='')
    l5.config(text='0')
    l7.config(text='0')
    l9.config(text='0')



from tkinter import *
win=Tk()
win.state('zoomed')
v=Label(text='Gym Membership Plans',font=('tahoma',30,'italic'))
lis=Listbox(font=('tahoma',20,'bold'),height=4)
lis.insert(0,'Monthly')
lis.insert(1,'Quarterly')
lis.insert(2,'Half-Yearly')
lis.insert(3,'Yearly')
l1=Label(font=('tahoma',20,'bold'))

btn1=Button(text='Show Cost',font=('tahoma',15,'bold'),command=showCost)

l2=Label(text='Enter number of memebers',font=('tahoma',20,'bold'))
t1=Entry(font=('tahoma',20,'bold'))
btn2=Button(text='Calculate',font=('tahoma',15,'bold'),command=getcal)

l3=Label(text='Student Discount? (Y/N)',font=('tahoma',20,'bold'))
t2=Entry(font=('tahoma',20,'bold'))

btn3=Button(text='Reset',font=('tahoma',15,'bold'),command=clear)
btn4=Button(text='Exit',font=('tahoma',15,'bold'),command=win.destroy)

l4=Label(text='Total',font=('tahoma',20,'bold'))
l5=Label(text='0',font=('tahoma',20,'bold'))
l6=Label(text='Discount',font=('tahoma',20,'bold'))
l7=Label(text='0',font=('tahoma',20,'bold'))
l8=Label(text='Net Payable Amount',font=('tahoma',20,'bold'))
l9=Label(text='0',font=('tahoma',20,'bold'))

v.pack()
lis.pack()
l1.pack()
btn1.pack()
l2.pack()
t1.pack()
l3.pack()
t2.pack()
l4.pack()
l5.pack()
l6.pack()
l7.pack()
l8.pack()
l9.pack()
btn2.pack()
btn3.pack()
btn4.pack()

win.mainloop()