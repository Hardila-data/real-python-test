#Update sql

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    #Update data
    c.execute("UPDATE population SET population = 900000 where city='New York City'")
    
    #Delete data
    c.execute("DELETE FROM population WHERE city='Boston'")

    print("\nNEW DATA:\n")
    c.execute("SELECT * FROM population")
    rows = c.fetchall()
    for r in rows:
        print(r[0], r[1], r[2])
