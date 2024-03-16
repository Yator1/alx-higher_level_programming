#!/usr/bin/python3

"""
a script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
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
    my_query = "SELECT * FROM states;"
    cur.execute(my_query)

    #obtaining query results
    states_starting_with_N = cur.fetchall()
    for state in states_starting_with_N:
        if state[1][0] == 'N':
            print(state)

    cur.close()
    my_db.close()
