#!/usr/bin/python3

"""
a script that takes in the name of a state as an argument
lists all cities of that state, using the database hbtn_0e_4_usa
"""


import MySQLdb
import sys


def filter_city_state():
    """
    takes state as an argument and lista all cities of that state
    Results must be sorted in ascending order by cities.id
    """
    if len(sys.argv) != 5:
        return

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities\
                LEFT JOIN states\
                ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id", (sys.argv[4],))

    query_rows = cur.fetchall()
    string = ""
    for row in query_rows:
        if (row[2] == sys.argv[4]):
            string += row[1] + ", "
    print(string[:-2])

    cur.close()
    db.close()


if __name__ == "__main__":
    filter_city_state()
