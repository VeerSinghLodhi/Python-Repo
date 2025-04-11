from tkinter import *
w=Tk()
w.state('zoomed')
w.title('Employee Emergency Information')
l1=Label(text='Employee Emergency Information',font=('tahoma',35,'normal'),fg='black')
l2=Label(text='We\'ll use these details only during emergency situations. Please give accurate information',font=('tahoma',15,'italic'),fg='black')
l3=Label(text='Full Name',font=('tahoma',14,'normal'))
l4=Label(text='Age',font=('tahoma',14,'normal'))
l5=Label(text='Blood Group',font=('tahoma',14,'normal'))
l6=Label(text='Emergency Contact Number',font=('tahoma',14,'normal'))
l7=Label(text='Do you have any long term illness?',font=('tahoma',14,'normal'))



t1=Entry(font=('tahoma',14,'normal'))
t2=Entry(font=('tahoma',14,'normal'))
t3=Entry(font=('tahoma',14,'normal'))

ch1=Listbox(font=('tahoma',14,'bold'))
blood_group=['A-positive (A+)','A-negative (A−)','B-positive (B+)','B-negative (B−)','AB-positive (AB+)','AB-negative (AB−)','O-positive (O+)','O-negative (O−)']
i=0
for bg in blood_group:
    ch1.insert(i,bg)
    i+=1
    
rb1=Radiobutton(text='Yes',font=('tahoma',14,'bold'),value=1)
rb2=Radiobutton(text='No',font=('tahoma',14,'bold'),value=2)

l1.pack()
l2.pack()
l3.pack()
t1.pack()
l4.pack()
t2.pack()
l5.pack()
ch1.pack()
l6.pack()
t3.pack()
l7.pack()
rb1.pack()
rb2.pack()
w.mainloop()
