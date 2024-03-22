#!/usr/bin/python3

"""
a script that creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City, Base


def relationship_state_cities():
    if len(sys.argv) != 4:
        return

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    session.add(new_state)
    session.commit()
    new_city = City(name="San Francisco", state=new_state)
    session.add(new_city)
    session.commit()

    session.close()


if __name__ == "__main__":
    relationship_state_cities()
