#Create a SQLite3 database table

#import the sqlite3 library
import sqlite3

#Create a new database if does not exist
conn = sqlite3.connect("new.db")

#Get a cursor object used to execute SQL Commands
cursor = conn.cursor()

#create table
cursor.execute("""CREATE TABLE population
                (city TEXT, state TEXT, population INT)""")

#Close the database connection
conn.close()