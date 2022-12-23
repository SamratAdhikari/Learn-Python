# Update and Delete Data in Database

import sqlite3

mydb = sqlite3.connect("tutorial.db")
cursor = mydb.cursor()

def update():
    query = "UPDATE stuffToPlot SET value = 99 WHERE value = 0"
    cursor.execute(query)
    mydb.commit()

    # show data
    query = "SELECT * FROM stuffToPlot"
    cursor.execute(query)

    [print(row) for row in cursor.fetchall()]
    print(50*"#")

def deleteIT():
    query = "DELETE FROM stuffToPlot WHERE value = 3 LIMIT 1"
    cursor.execute(query)
    mydb.commit()

    # show data
    query = "SELECT * FROM stuffToPlot"
    cursor.execute(query)
    
    [print(row) for row in cursor.fetchall()]



update()
deleteIT()

mydb.close()
