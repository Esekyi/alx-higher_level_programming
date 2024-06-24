#!/usr/bin/python3

"""
Python script that lists all states with a name depending on a user input from the database hbtn_0e_0_usa
All important parameters and the user input would be passed as arguments to the script. Using the MySQLdb module. 
In all 4 arguments, the first 3 are the database credentials and the last one is the user input
"""
import MySQLdb
import sys

args = sys.argv
user = args[1]
password = args[2]
db_name = args[3]
name = args[4]

db = MySQLdb.connect(host='localhost', port=3306,
                     user=user, passwd=password, db=db_name)
cur = db.cursor()
cur.execute("SELECT id, name FROM states WHERE name LIKE '{}%' ORDER BY id ASC".format(name))
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
db.close()