#!/usr/bin/python3
""" 0-select_states """

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    """Classe représentant la table states"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # Création de l'URL de connexion
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    # Création d'une session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête pour récupérer tous les états, triés par id
    states = session.query(State).order_by(State.id).all()

    # Affichage des résultats
    for state in states:
        print("({}, '{}')".format(state.id, state.name))

    # Fermeture de la session
    session.close()
