#!/usr/bin/python3
'''Prints all City objects from the database hbtn_0e_14_usa'''
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_city import City

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
        for state, city in session.query(State, City).filter(
                State.id == City.state_id):
            print("{}: ({}) {}".format(state.name, city.id, city.name))
