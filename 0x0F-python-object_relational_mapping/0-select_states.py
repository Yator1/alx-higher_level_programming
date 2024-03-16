#!/usr/bin/python3

"""
a script that takes in an argument
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb


if __name__ == "__main__":
    import sys

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
