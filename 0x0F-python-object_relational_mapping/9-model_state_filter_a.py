#!/usr/bin/python3
"""module"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    dbUser, dbPass, dbName = argv[1], argv[2], argv[3]

    dbURL = "mysql+mysqldb://{}:{}@localhost:3306/{}" \
        .format(dbUser, dbPass, dbName)
    engine = create_engine(dbURL)
    Session = sessionmaker(engine)
    s = Session()
    states = s.query(State).filter(State.name.contains('a')) \
        .order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
    s.commit()
    s.close()
