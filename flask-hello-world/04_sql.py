import csv
import sqlite3

with sqlite3.connect("new.db") as connection:
    cursor = connection.cursor()

    #Open CSV employees
    employees = csv.reader(open("employees.csv", "rU"))
    employees_tuple = list(map(tuple, employees))
    print(employees_tuple)


    #create a table call employees
    # cursor.execute("CREATE TABLE employess(firstname TEXT, lastname TEXT)")

    cursor.executemany('INSERT INTO employess(firstname, lastname)  VALUES(?,?)', employees_tuple)

    # cursor.commit()

    # cursor.close()

