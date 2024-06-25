#!/usr/bin/python3
"""
Python Script lists all State objects that contain the letter `a`
from the database hbtn_0e_6_usa
this script takes 3 arguments: mysql username,
mysql password and database name
using the module SQLAlchemy
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Main function
    get access to the database and
    get all state that contain the letter a
    """
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(user, password, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name.contains('a'))
    if state is not None:
        for instance in state:
            print("{0}: {1}".format(instance.id, instance.name))
    # session.close()
