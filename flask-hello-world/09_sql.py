# JOINing data from multiple tables


import sqlite3

with sqlite3.connect("new.db") as connection:
    
    cursor = connection.cursor()

    # cursor.execute("""SELECT population.city, population.population, regions.region FROM population, regions WHERE \
                    # population.city = regions.city""")
    cursor.execute("""SELECT population.city, population.population, regions.region FROM population INNER JOIN regions \
                     ON population.city = regions.city""")

    # cursor.execute("SELECT count(population.city) FROM population ")

    rows = cursor.fetchall()

    for row in rows:
        print("City: " + row[0])
        print("Population: " + str(row[1]))
        print("Region: "+ row[2])
        print("")
        # print(row)