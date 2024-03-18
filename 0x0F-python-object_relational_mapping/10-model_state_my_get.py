#!/usr/bin/python3

"""
a script that prints the State id object with the name passed as
argument from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_a_state():
    """
    -use the module SQLAlchemy
    -using 4 arguments:
    mysql username, mysql password, database name & name to search
    """
    if len(sys.argv) != 5:
        return

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    key = 0
    for state in session.query(State):
        if sys.argv[4] == state.name:
            print("{}".format(state.id))
            key = 1
    if key == 0:
        print("Not found")
    session.close()


if __name__ == "__main__":
    get_a_state()
