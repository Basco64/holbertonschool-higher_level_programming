#!/usr/bin/python3
""" 9-model_state_filter_a.py """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Create database
    # pool_pre_ping verifies connection to the database
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and display
    states_filtered = session.query(State).filter(State.name.contains('a'))
    for state in states_filtered.order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()
