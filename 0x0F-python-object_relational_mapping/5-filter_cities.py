#!/usr/bin/python3

"""
Python script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
This script takes in 4 arguments: the username, password,
database name, and state name (SQL injection free!).
"""

import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    user = args[1]
    password = args[2]
    db_name = args[3]
    state_name = args[4]
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=user, passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("""SELECT id, name FROM cities WHERE state_id =
    (SELECT id FROM states WHERE name = %s) ORDER BY id ASC""", (state_name,))
    print_rows = cur.fetchall()

    if print_rows is not None:
        print(", ".join(row[1] for row in print_rows))
    else:
        print("")

    cur.close()
    db.close()
