#!/usr/bin/python3

"""
script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def states_with_a():
    """
    -use the module SQLAlchemy
    -using 3 arguments:
    mysql username, mysql password and database name
    """
    if len(sys.argv) != 4:
        return

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    States = session.query(State).order_by(State.id)

    for state in States:
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    states_with_a()
