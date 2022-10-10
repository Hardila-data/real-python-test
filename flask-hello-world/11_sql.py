import sqlite3


prompt = """Select the operation that you want to perform [1-5]:
        1.Average
        2.Max
        3.Min
        4.Sum
        5.Exit
        """

with sqlite3.connect("newnum.db") as connection:

    cursor = connection.cursor()

    while True:

        x= input(prompt)

        if x in set(["1","2","3","4"]):
            operation = {1:"AVG", 2:"MAX", 3:"MIN", 4:"SUM"}[int(x)]

            cursor.execute("SELECT {}(num) from numbers".format(operation))
            
            get = cursor.fetchone()

            print(operation + ": %f" %get[0])
        
        elif x=="5":
            print("Exit")

            break



