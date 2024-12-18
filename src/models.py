import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'person'
    
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    fecha_suscripcion = Column(DateTime(timezone=True), nullable=False)

class Planet(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name =  Column(String(250), nullable=False)


class Character(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    name =  Column(String(250), nullable=False)

class Vehicle(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    name =  Column(String(250), nullable=False)

class Favorite (Base):
    __tablename__ = 'favorite'

    id = Column(Integer, primary_key=True)
    name =  Column(String(250), nullable=False)

class Create(Base):
    __tablename__ = 'create'
    id = Column(Integer, primary_key=True)
    user_id =  Column(String(250), nullable=False)
    name =  Column(String(250), nullable=False)

class Data(Base):
    __tablename__ = 'create'
    id = Column(Integer, primary_key=True)
    user_id =  Column(String(250), nullable=False)
    name =  Column(String(250), nullable=False)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy baseñ{}
render_er(Base, 'diagram.png')
