#!/usr/bin/python3
"""
Module contsining a script that takes
the name of a state as an argument and
lists all the cities in that state
using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    state = sys.argv[4]
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states INNER JOIN cities ON states.state_id = "\
        "cities.id WHERE states.name = " + sys.argv[4]
    print(query)
    cur.close()
    db.close()
