# TreeView with Search Feature

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import mysql.connector as mc
from tkinter import messagebox as msg

# functions
def update(rows):
	trv.delete(*trv.get_children())
	for i in rows:
		trv.insert("", "end", values=i)

def search():
	ans = q.get()
	query = "SELECT id, first_name, last_name, age FROM customers WHERE first_name LIKE '%"+ans+"%' OR last_name LIKE '%"+ans+"%'"
	cursor.execute(query)
	rows = cursor.fetchall()
	update(rows)

def clear():
	query = "SELECT id, first_name, last_name, age FROM customers"
	cursor.execute(query)
	rows = cursor.fetchall()
	update(rows)

def getrow(event):
	# rowid = trv.identify_row(event.y)
	item = trv.item(trv.focus())
	# print(item["values"][0])
	t1.set(item["values"][0])
	t2.set(item["values"][1])
	t3.set(item["values"][2])
	t4.set(item["values"][3])


def add_cust():
	# custid = t1.get()
	fname = t2.get()
	lname = t3.get()
	age = t4.get()
	query = "INSERT INTO customers(id, first_name, last_name, age) VALUES(NULL, %s, %s, %s)"
	# cursor.execute(query, (custid, fname, lname, age))
	cursor.execute(query, (fname, lname, age))
	msg.showinfo("Done", "Customer Added!")
	mydb.commit()
	clear()

def update_cust():
	fname = t2.get()
	lname = t3.get()
	age = t4.get()
	custid = t1.get()

	ask = msg.askquestion("Confirm Update", "Are you sure you want to update the customer?")
	print("test1")
	if ask == "yes":
		query = "UPDATE customers SET first_name = %s, last_name = %s, age = %s WHERE id = %s"
		cursor.execute(query, (fname, lname, age, custid))
		mydb.commit()
		msg.showinfo("Done", "Customer Data Updated!")
		clear()


def remove_cust():
	customer_id = t1.get()
	ask = msg.askquestion("Confirm Delete", "Are you sure you want to delete the customer?")
	if ask == "yes":
		query = "DELETE FROM customers WHERE id = " + customer_id
		cursor.execute(query)
		msg.showinfo("Done", "Customer Deleted!")
		mydb.commit()
		clear()


mydb = mc.connect(host="localhost", user="root", passwd="samratmetal123", database="Manager", auth_plugin="mysql_native_password")
cursor = mydb.cursor()

root = Tk()

wrapper1 = LabelFrame(root, text="Customer List")
wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame(root, text="Customer Data")

wrapper1.pack(fill=BOTH, expand="yes", padx=20, pady=10)
wrapper2.pack(fill=BOTH, expand="yes", padx=20, pady=10)
wrapper3.pack(fill=BOTH, expand="yes", padx=20, pady=10)

trv = ttk.Treeview(wrapper1, columns=(1,2,3,4), show="headings", height="6")
trv.pack()

trv.heading(1, text="Customer ID")
trv.heading(2, text="First Name")
trv.heading(3, text="Last Name")
trv.heading(4, text="Age")

trv.bind("<Double-1>", getrow)

query = "SELECT id, first_name, last_name, age from customers"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)

# Search Section
q = StringVar()

l1 = Label(wrapper2, text="Search")
l1.pack(side=tk.LEFT, padx=10)

e = Entry(wrapper2, textvar=q)
e.pack(side=tk.LEFT, padx=10)


b = Button(wrapper2, text="Search", font="times 12", borderwidth=3, relief=RAISED, bg="steel blue", fg="white", command=search)
b.pack(side=tk.LEFT, padx=10)
clear_b = Button(wrapper2, text="Clear", font="times 12", borderwidth=3, relief=RAISED, bg="steel blue", fg="white", command=clear)
clear_b.pack(side=tk.LEFT, padx=10)


# User Data Section
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()

l1 = Label(wrapper3, text="Customer ID")
l1.grid(row=0, column=0, padx=5, pady=5, sticky=W)
e1 = Entry(wrapper3, textvar=t1)
e1.grid(row=0, column=1, padx=5, pady=5)

l2 = Label(wrapper3, text="First Name")
l2.grid(row=1, column=0, padx=5, pady=5, sticky=W)
e2 = Entry(wrapper3, textvar=t2)
e2.grid(row=1, column=1, padx=5, pady=5)

l3 = Label(wrapper3, text="Last Name")
l3.grid(row=2, column=0, padx=5, pady=5, sticky=W)
e3 = Entry(wrapper3, textvar=t3)
e3.grid(row=2, column=1, padx=5, pady=5)

l4 = Label(wrapper3, text="Age")
l4.grid(row=3, column=0, padx=5, pady=5, sticky=W)
e4 = Entry(wrapper3, textvar=t4)
e4.grid(row=3, column=1, padx=5, pady=5)

insert_btn = Button(wrapper3, text="Add Client", font="times 12", borderwidth=3, relief=RAISED, bg="steel blue", fg="white",  command=add_cust)
update_btn = Button(wrapper3, text="Update Client", font="times 12", borderwidth=3, relief=RAISED, bg="steel blue", fg="white", command=update_cust) 
remove_btn = Button(wrapper3, text="Remove Client", font="times 12", borderwidth=3, relief=RAISED, bg="steel blue", fg="white", command=remove_cust) 
insert_btn.grid(row=4, column=0, padx=5, pady=3)
update_btn.grid(row=4, column=1, padx=5, pady=3)
remove_btn.grid(row=4, column=2, padx=5, pady=3)

root.title("TreeView")
root.geometry("800x600")
root.mainloop()
