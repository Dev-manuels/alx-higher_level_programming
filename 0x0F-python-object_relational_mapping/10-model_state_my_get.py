#!/usr/bin/python3
"""
Module containing a script that prints the State object
with the name passed as argument from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    import sys
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    find_state = sys.argv[4]
    if ";" not in find_state:
        db = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
            .format(sys.argv[1], sys.argv[2], sys.argv[3])
        engine = create_engine(db, pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()

        result = session.query(State).filter(State.name == find_state).all()
        if result:
            for row in result:
                print(f"{row.id}")
        else:
            print("Not found")
