# Create Form and Insert Data

from tkinter import *
import tkinter as tk
import mysql.connector as mc


mydb = mc.connect(host="localhost", user="root", passwd="samratmetal123", database="Manager", auth_plugin="mysql_native_password")
cursor = mydb.cursor()

# Functions
def addcust():
	cust_id = e1.get()
	fname = e2.get()
	lname = e3.get()
	age = e4.get()
	
	sql = "INSERT INTO customers VALUES(%s, %s, %s, %s)"
	cursor.execute(sql, (cust_id, fname, lname, age))
	mydb.commit()
	print("Customer Added")

root = Tk()
root.title("Customer Form")
root.geometry("350x350")
root.resizable(False, False)

f1 = Frame(root)
f1.pack(side=tk.LEFT, padx=20)

cust_id = StringVar()
fname = StringVar()
lname = StringVar()
age = StringVar()


l1 = Label(f1, text="Customer id")
l1.grid(row=0, column=1)


e1 = Entry(f1, textvar=cust_id)
e1.grid(row=0, column=2, padx=10)

l2 = Label(f1, text="First Name")
l2.grid(row=1, column=1, sticky=W)

e2 = Entry(f1, textvar=fname)
e2.grid(row=1, column=2, padx=10)

l3 = Label(f1, text="Last Name")
l3.grid(row=2, column=1, sticky=W)

e3 = Entry(f1, textvar=lname)
e3.grid(row=2, column=2, padx=10)

l4 = Label(f1 , text="Age")
l4.grid(row=3, column=1, sticky=W)

e4 = Entry(f1, textvar=age)
e4.grid(row=3, column=2, padx=10)


b = Button(f1, text="Add", font="times 15", command=addcust)
b.grid(row=5, column=2, sticky=W, pady=10)





root.mainloop()

