#!/usr/bin/python3
"""
Python script that lists all cities from the database hbtn_0e_4_usa.
This script takes in 3 arguments: the username, password, and database name.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    user = args[1]
    password = args[2]
    db_name = args[3]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=user, passwd=password, db=db_name)
    cur = db.cursor()

    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities INNER
                JOIN states ON cities.state_id = states.id ORDER
                BY cities.id ASC""")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
