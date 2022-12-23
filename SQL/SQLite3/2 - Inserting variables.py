# Inserting Variables to Database

import sqlite3
import time
import datetime
import random

mydb = sqlite3.connect("tutorial.db")
cursor = mydb.cursor()


def create_table():
    query = "CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datastamp TEXT, keyword TEXT, value REAL)"
    cursor.execute(query)


def data_entry():
    cursor.execute("INSERT INTO stuffToPlot VALUES(145323, '2016-01-01', 'Python', 5)")
    mydb.commit()


def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime("%Y-%m-%d %H:%M:%S"))
    keyword = "Python"
    value = random.randrange(0, 10)

    query = "INSERT INTO stuffToPlot(unix, datastamp, keyword, value) VALUES(?, ?, ?, ?)"
    cursor.execute(query, (unix, date, keyword, value))
    mydb.commit()


# create_table()
# for i in range(10):
#     dynamic_data_entry()
#     time.sleep(1)


cursor.close()
mydb.close()
