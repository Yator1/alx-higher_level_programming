#!/usr/bin/python3

"""
script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb

if __name__ == '__main__':
    import sys

    # Connecting to MySQL database
    my_db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )

    #creating a cursor
    cur = my_db.cursor()

    #executing MySQL queries
    cur.execute("SELECT * FROM states WHERE name = '{}' \
            ORDER BY id ASC".format(sys.argv[4]))

    #obtaining query results
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    my_db.close()
