#!/usr/bin/python3

"""
Python script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
All important parameter would be passed as arguments to
the script. Using the MySQLdb module
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
    cur.execute(
        "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
