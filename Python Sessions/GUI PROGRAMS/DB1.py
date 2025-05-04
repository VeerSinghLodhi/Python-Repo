import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",password="manager",database="veer")
sql="insert into  student values(102,'B')"
cursor=db.cursor()
cursor.execute(sql)
db.commit()
print("Data Saved")