#!/usr/bin/python3
"""
Module containing a script that deletes
all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    db = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db, pool_pre_ping=True)
    Session = sessionmaker()
    session = Session(bind=engine)

    result = session.query(State).filter(State.name.like("%a%")).all()
    if result:
        for state in result:
            session.delete(state)
        session.commit()
