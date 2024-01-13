#!/usr/bin/python3
"""module"""
from sys import argv
from sqlalchemy.engine.url import URL
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    dbUser, dbPass, dbName = argv[1], argv[2], argv[3]

    dbURL = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(dbUser, dbPass, dbName)
    engine = create_engine(dbURL, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    s = Session()
    states = s.query(State).all()
    for state in states:
        print(f"{state.id}: {state.name}")
    s.commit()
    s.close()
