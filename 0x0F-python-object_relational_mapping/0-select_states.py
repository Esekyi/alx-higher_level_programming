#!/usr/bin/python3
"""
Thsi script prints all states from the database hbtn_0e_0_usa
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
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    print_rows = cur.fetchall()
    for row in print_rows:
        print(row)

    cur.close()
    db.close()
