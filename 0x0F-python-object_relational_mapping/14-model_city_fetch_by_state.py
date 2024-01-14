#!/usr/bin/python3
"""module"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    db_user, db_pass, db_name = argv[1:4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(db_user, db_pass, db_name))
    s = sessionmaker()(bind=engine)
    rows = s.query(City, State) \
        .filter(State.id == City.state_id).order_by(City.id).all()
    for row in rows:
        city, state = row._tuple()
        print(f"{state.name}: ({city.id}) {city.name}")
