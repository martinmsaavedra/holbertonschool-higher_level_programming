#!/usr/bin/python3
from model_state import Base, State
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # HERE: no SQL query, only objects!
    for state in session.query(State).order_by(State.id).all():
        for letter in state.name:
            if (letter == 'a'):
                print("{}: {}".format(state.id, state.name))
                break
    session.close()
