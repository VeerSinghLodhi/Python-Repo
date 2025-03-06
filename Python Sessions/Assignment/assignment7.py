
job=input("Enter Job(M for Manager, R for Regular Worker ): ")
experience=int(input("Enter Experience:"))
ans=0
if job=="M" or job=="m" and experience>0:
    if experience>10:
        salary=10000
    elif experience>=5 and experience<=10:
        salary=8000
    elif experience<5:
        salary=6000
    ans=1
elif job=="R" or job=="r" and experience>0:
    if experience>10:
        salary=8000
    elif experience>=5 and experience<=10:
        salary=6000
    elif experience<5:
        salary=4000
    ans=1
else:
    print("Invalid Job/Experience")
if ans==1:
    print("Your salary is  :",salary)
