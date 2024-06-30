#!/usr/bin/python3
"""
Python script that fetches and prints all cities by state
from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    """
    Main function
    Access to the database and fetch
    all cities by state
    """
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    city = session.query(City, State).join(
        State, City.state_id == State.id).order_by(City.id).all()

    for city, state in city:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
