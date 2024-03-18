#!/usr/bin/python3

"""
a script that prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def first_states_sql():
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

    States = session.query(State).order_by(State.id).first()

    if States:
        print("{}: {}".format(States.id, States.name))
    else:
        print("nothing")
    session.close()


if __name__ == "__main__":
    first_states_sql()
