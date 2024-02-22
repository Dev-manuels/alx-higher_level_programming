#!/usr/bin/python3
"""
Module containing a script that changes the name of
a State object from the database hbtn_0e_6_usa
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

    tmp_obj = session.query(State).filter(State.id == 2).one()
    tmp_obj.name = "New Mexico"

    session.commit()
