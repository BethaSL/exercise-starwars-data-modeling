import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User (Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(220), nullable=False)
    password = Column(String(10), nullable=False)

    favorites= relationship("Favorites", back_populates="parent")


class Favorites (Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey("user.id"))
    
    user= relationship("User", back_populates="children")
    planets= relationship("Planets", back_populates="parent")
    characters= relationship("Characters", back_populates="parent")


class Planets (Base):
    __tablename__ = 'planets'
    id = Column(String, primary_key=True)
    name_planet = Column(String, nullable=False)
    population = Column(Integer, nullable=False)
    review_planet = Column(String, nullable=False)
    favorites_id= Column(Integer, ForeignKey("favorites.id"))

    favorites= relationship("Favorites", back_populates="children")


class Characters (Base):
    __tablename__ = 'characters'
    id = Column(String, primary_key=True)
    name_character = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    review_character = Column(String, nullable=False)
    favorites_id= Column(Integer, ForeignKey("favorites.id"))

    favorites= relationship("Favorites", back_populates="children")

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')