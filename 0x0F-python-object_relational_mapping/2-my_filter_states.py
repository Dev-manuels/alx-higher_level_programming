#!/usr/bin/python3
"""
Module containing a script that takes in an argument
and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb


if __name__ == "__main__":
    find_name = sys.argv[4]
    # create DB connection
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    # create cusor object
    cur = db.cursor()
    # create query
    query = "SELECT * FROM states WHERE BINARY name = '{}' \
        ORDER BY states.id".format(find_name)
    # Execute query
    cur.execute(query)
    rows = cur.fetchall()
    # print result
    for row in rows:
        print(row)

    # clean up
    cur.close()
    db.close()
