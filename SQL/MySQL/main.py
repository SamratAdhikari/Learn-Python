import mysql.connector as mc

mydb = mc.connect(host="localhost", user="root", passwd="samratmetal123", database="samrat")
mycursor = mydb.cursor()
# mycursor.execute("show databases")


mycursor.execute("select * from student")
# for i in mycursor:
#     print(i)

result = mycursor.fetchone()
print(result)
exit()

result = mycursor.fetchall()
print(result)



