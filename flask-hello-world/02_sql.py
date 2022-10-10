import sqlite3
from tokenize import cookie_re

#Create connection
conn = sqlite3.connect("new.db")

#Get a cursor object
cursor = conn.cursor()

#insert data
cursor.execute("INSERT INTO population VALUES('New York City',\
    'NY', 84000000)")

cursor.execute("INSERT INTO population VALUES('San Francisco',\
    'CA', 800000)")

#Commint changes
conn.commit()

#Close the database connection
conn.close()