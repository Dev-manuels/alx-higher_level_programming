#!/usr/bin/python3
"""
Module containing a script that lists all states
with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    #create DB connection
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    #create cusor object
    cur = db.cursor()
    #create query
    query = "SELECT * FROM states WHERE name={} ORDER BY id ASC".format(sys.argv[4])
    #Execute query
    cur.execute(query)
    rows = cur.fectchall()
    #print result
    for row in rows:
        print(row)

    #clean up
    cur.close()
    db.close()
        
