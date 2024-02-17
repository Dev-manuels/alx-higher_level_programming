#!/usr/bin/python3
"""
Module containing script that lists all states
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Create db Connection
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    # Create a cursor object
    cur = db.cursor()
    # execute select query
    cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()
    # display result of select query
    for row in rows:
        print(row)

    # Clean up actions
    cur.close()
    db.close()
