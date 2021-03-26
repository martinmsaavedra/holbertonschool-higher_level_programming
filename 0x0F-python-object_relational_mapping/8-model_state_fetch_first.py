#!/usr/bin/python3
'''Prints the first State object from the database hbtn_0e_6_usa'''
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # HERE: no SQL query, only objects!
    state = session.query(State).order_by(State.id).all()
    if len(state) == 0:
        print("Nothing")
    else:
        print("{}: {}".format(state[0].id, state[0].name))
    session.close()
