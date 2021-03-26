#!/usr/bin/python3
'''Lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = []
    for state, city in session.query(State, City).filter(State.id == City.state_id).all():
        if (state.id not in states):
            print("{}: {}".format(state.id, state.name))
            states.append(state.id)
        print("\t{}: {}".format(city.id, city.name))
