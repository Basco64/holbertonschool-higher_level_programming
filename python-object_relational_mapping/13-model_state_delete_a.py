#!/usr/bin/python3
""" 11-model_state_insert.py """

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
    query_state = session.query(State)
    states_to_delete = query_state.filter(State.name.contains('a')).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    # Close session
    session.close()
