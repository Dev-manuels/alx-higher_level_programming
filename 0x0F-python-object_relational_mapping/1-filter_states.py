#!/usr/bin/python3
"""
Module containing script that lists all states
with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Create db Connection
    db = MySQLdb.connect(host="localhost", port="3306", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    # Create a cursor object
    cur = db.cursor()
    # execute select query
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    # display result of select query
    for row in rows:
        print(row)

    # Clean up actions
    cur.close()
    db.close()
