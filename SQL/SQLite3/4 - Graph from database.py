# Graph from database

import sqlite3 as sq
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
import datetime

style.use("fivethirtyeight")

mydb = sq.connect("tutorial.db")
cursor = mydb.cursor()

def graph_data():
    query = "SELECT unix, value FROM stuffToPlot"
    cursor.execute(query)
    dates = []
    values = []
    for row in cursor.fetchall():
        print(row[0])
        # print(datetime.datetime.fromtimestamp(row[0]))
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-')
    plt.show()




graph_data()

mydb.close()
