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
    find_state = sys.argv[4]
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT cities.name FROM cities INNER JOIN states ON \
        cities.state_id = states.id WHERE states.name ='{}'".format(find_state)
    rows = cur.execute(query)
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))
    cur.close()
    db.close()
