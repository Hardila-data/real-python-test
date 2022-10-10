import sqlite3

with sqlite3.connect("new.db") as connection:
    c= connection.cursor()

    for row in c.execute("SELECT firstname, lastname from employess"):
        print(row[0], row[1]) 

    print("\nPrint with fetch all")
    c.execute("SELECT firstname, lastname from employess")
    rows = c.fetchall()
    for r in rows:
        print(r[0], r[1])