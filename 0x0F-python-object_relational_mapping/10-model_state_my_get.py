#!/usr/bin/python3
"""
Python Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
this script takes 4 arguments: mysql username, mysql password,
database name and state name to search (SQL injection free)
using the module SQLAlchemy
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Main function
    Access to the database and get the state
    a user passed as argument
    """
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(user, password, db_name),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_query = session.query(State).filter(State.name == state_name).first()
    if state_query is not None:
        print("{0}".format(state_query.id))
    else:
        print("Not found")
    session.close()
