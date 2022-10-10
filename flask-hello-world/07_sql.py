import sqlite3

with sqlite3.connect("new.db") as connection:

    cursor = connection.cursor()
    
    #Insert multiple records usign a tuple
    cities = [
                ('Boston', 'MA', 600000),
                ('Los Angeles', 'CA', 38000000),
                ('Houston', 'TX', 2100000),
                ('Philadelphia', 'PA', 1500000),
                ('San Antonio', 'TX', 1400000),
                ('San Diego', 'CA', 130000),
                ('Dallas', 'TX', 1200000),
                ('San Jose', 'CA', 900000),
                ('Jacksonville', 'FL', 800000),
                ('Indianapolis', 'IN', 800000),
                ('Austin', 'TX', 800000),
                ('Detroit', 'MI', 700000)
                ]

    cursor.executemany("INSERT INTO population values(?,?,?)", cities)

    cursor.execute("SELECT * FROM population WHERE population>1000000")

    rows = cursor.fetchall()
    
    for row in rows:
        print(row)