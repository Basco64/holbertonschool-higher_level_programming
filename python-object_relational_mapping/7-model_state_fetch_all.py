#!/usr/bin/env python3
""" First state model """
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class State(Base):
    """State class"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


engine = create_engine(
  'mysql+mysqldb://username/:password@localhost:3306/db_name',
  pool_pre_ping=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_state = State(name='California')
session.add(new_state)
session.commit()
