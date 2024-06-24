#!/usr/bin/python3

"""
Python script that lists all states with a name depending
on a user input from the database hbtn_0e_0_usa
All important parameters and the user input would be passed
as arguments to the script. Using the MySQLdb module.
In all 4 arguments, the first 3 are the database credentials
and the last one is the user input.
The case here is there won't be any SQL injection. This script is
safe from MySQL injections!
"""
import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    user = args[1]
    password = args[2]
    db_name = args[3]
    name = args[4]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=user, passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute(
        "SELECT id, name FROM states WHERE name LIKE %s ORDER BY id ASC",
        (name+'%',))
    print_rows = cur.fetchall()

    for row in print_rows:
        print(row)

    cur.close()
    db.close()
