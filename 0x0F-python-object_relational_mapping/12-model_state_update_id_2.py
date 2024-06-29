#!/usr/bin/python3
"""
Python Script that changes the name of a State
object from the database hbtn_0e_6_usa
it takes 4 arguments: mysql username, mysql password,
database name and the new name of the state
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Main function
    Access to the database and update the state
    with a new name
    """
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    update_state = session.query(State).filter(State.id == 2).first()
    update_state.name = "New Mexico"
    session.commit()
    session.close()
