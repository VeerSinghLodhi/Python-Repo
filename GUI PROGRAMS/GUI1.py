
def calc():
    print('veer')
    price=float(t1.get())
    qty=float(t2.get())
    total=price*qty
    if total>1000:
        dis=total*5/100
    else:
        dis=0
    if dis==0:
        t4.config(fg='red')
    else:
        t4.config(fg='blue')
    net=total-dis
    t3.delete(0,END)
    t4.delete(0,END)
    t5.delete(0,END)
    t3.insert(0,total)
    t4.insert(1,dis)
    t5.insert(0,net)

def clear():
    print('Rajendra')
    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)
    t4.delete(0,END)
    t5.delete(0,END)
    t1.focus()

from tkinter import *
window=Tk()
window.state('zoomed')

l1=Label(text='Enter Price of Product',font=('tahoma',20,'bold'))
l2=Label(text='Enter Quantity',font=('tahoma',20,'bold'))
l3=Label(text='Total',font=('tahoma',20,'bold'))
l4=Label(text='Discount',font=('tahoma',20,'bold'))
l5=Label(text='Net Payable',font=('tahoma',20,'bold'))


t1=Entry(font=('tahoma',20,'bold'))
t2=Entry(font=('tahoma',20,'bold'))
t3=Entry(font=('tahoma',20,'bold'))
t4=Entry(font=('tahoma',20,'bold'))
t5=Entry(font=('tahoma',20,'bold'))

b1=Button(text='OK',font=('tahoma',20,'bold'),command=calc)
b2=Button(text='Clear',font=('tahoma',20,'bold'),command=clear)

l1.pack()
t1.pack()
l2.pack()
t2.pack()
l3.pack()
t3.pack()
t2.pack()
l4.pack()
t4.pack()
l5.pack()
t5.pack()
b1.pack()
b2.pack()




window.mainloop()