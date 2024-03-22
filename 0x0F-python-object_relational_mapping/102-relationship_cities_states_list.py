#!/usr/bin/python3


"""
a script that lists all City objects from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City, Base


def list_cities():
    if len(sys.argv) != 4:
        return

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(state.id, state.name, state.state.name))

    session.close()


if __name__ == "__main__":
    list_cities()
