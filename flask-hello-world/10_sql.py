#Create database and Insert random data

import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:

    cursor = connection.cursor()

    #delete database table if exist
    cursor.execute("DROP TABLE if exists numbers")

    #Create database table
    cursor.execute("CREATE TABLE numbers(num INT)")

    for i in range(100):
        cursor.execute("INSERT INTO numbers VALUES(?)", (random.randint(0,100),))
