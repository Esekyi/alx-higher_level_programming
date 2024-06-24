#!/usr/bin/python3
"""
Python Script that lists all State objects from the database hbtn_0e_6_usa
this script takes 3 arguments: mysql username, mysql password and database name
using the module SQLAlchemy
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Main function
    """
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(user, password, db_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    session = session()

    for instance in session.query(State).order_by(State.id).all():
        print("{}: {}".format(instance.id, instance.name))
    session.close()
