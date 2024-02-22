#!/usr/bin/python3
"""
Module containing script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from model_state import State, Base
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    import sys

    db = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State()
    new_state.name = "Louisiana"

    session.add(new_state)
    session.commit()

    result = session.query(State).filter(State.name == new_state.name).all()
    if result:
        for row in result:
            print(row.id)
        else:
            pass
