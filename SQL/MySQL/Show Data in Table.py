# Show data in table

from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector as mc


mydb = mc.connect(host="localhost", user="root", passwd="samratmetal123", database="Test", auth_plugin="mysql_native_password")
cursor = mydb.cursor()
sql = "SELECT * FROM customers"
cursor.execute(sql)
rows = cursor.fetchall()

total = cursor.rowcount
print(f"Total data entries {total}")

root = Tk()
root.title("Customer Data")
root.geometry("650x400")
root.resizable(False, False)

f = Frame(root)
f.pack(side=tk.LEFT, padx=20)

tv = ttk.Treeview(f, columns=(1,2,3), show="headings", height=5)
tv.pack()

tv.heading(1, text="Name")
tv.heading(2, text="Age")
tv.heading(3, text="Email")

for i in rows:
	tv.insert("", "end", values=i)


root.mainloop()