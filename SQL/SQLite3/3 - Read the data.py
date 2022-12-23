# Read From(Select) Database Table

import sqlite3

mydb = sqlite3.connect("tutorial.db")
cursor = mydb.cursor()


def read_from_db():
    query = "SELECT * FROM stuffToPlot"
    # query = "SELECT * FROM stuffToPlot WHERE value=3 AND keyword = 'Python'"
    # query = "SELECT * FROM stuffToPlot WHERE unix > 15159465"
    cursor.execute(query)
    data = cursor.fetchall()
    # print(data)
    for row in data:
        print(row[0])


read_from_db()

mydb.close()
