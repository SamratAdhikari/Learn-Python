import sqlite3
import time
import datetime
import random

mydb = sqlite3.connect("tutorial.db")
cursor = mydb.cursor()


def create_table():
    query = "CREATE TABLE IF NOT EXISTS sample(unix REAL, datastamp TEXT, keyword TEXT, value REAL)"
    cursor.execute(query)


def data_entry():
    cursor.execute("INSERT INTO sample VALUES(145323, '2016-01-01', 'Python', 5)")
    mydb.commit()
    mydb.close()


create_table()
data_entry()
