from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base = declarative_base()


class Animal(Base):
    __tablename__ = 'animal'

    name = Column(String, primary_key=True)

    food = Column(Integer)
    time = Column(Integer)
    sociality = Column(Integer)
    habitat = Column(Integer)
    climate = Column(Integer)
    games = Column(Integer)
    movement = Column(Integer)

    photo = Column(String)
    info = Column(String)


Session = sessionmaker(bind=engine)
session = Session()
