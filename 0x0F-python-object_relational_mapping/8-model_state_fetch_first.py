#!/usr/bin/python3
'''Prints the first State object from the database hbtn_0e_6_usa'''
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == '__main__':
    if (len(argv) == 4):
        username = argv[1]
        password = argv[2]
        dbname = argv[3]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, dbname), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)

        session = Session()
        state = session.query(State).order_by(State.id).first()
        if (not state):
            print("Nothing")
        else:
            print("{}: {}".format(state.id, state.name))
        session.close()
