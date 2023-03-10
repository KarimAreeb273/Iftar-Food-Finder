from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///iftar.db')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    full_name = Column(String())
    city = Column(String())
    restaurant = Column(String())
    menu = Column(String())
    rating = Column(Integer())

    def __repr__(self):
        return f'User(id={self.id}, ' + \
            f'full_name="{self.full_name}", ' + \
            f'city="{self.city}", ' + \
            f'restaurant="{self.restaurant}", ' + \
            f'menu="{self.menu}", ' + \
            f'rating={self.rating})'

class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer(), primary_key=True)
    city = Column(String())
    state = Column(String())

    restaurant_locations = Column(Integer(), ForeignKey('restaurants.id'))   
    iftar_time = Column(Integer(), ForeignKey('iftar_tables.id'))   

    def __repr__(self):
        return f'Location(id={self.id}, city="{self.city}", state="{self.state}")'

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    city = Column(String())
    menu = Column(String())

    location_id = Column(Integer(), ForeignKey('locations.id'))   

    def __repr__(self):
        return f'Restaurant(id={self.id}, name="{self.name}", city="{self.city}", menu="{self.menu}")'

class IftarTable(Base):
    __tablename__ = 'iftar_tables'

    id = Column(Integer(), primary_key=True)
    state = Column(String())
    iftar_time = Column(String())
    location_id = Column(Integer(), ForeignKey('locations.id'))

    def __repr__(self):
        return f'IftarTable(id={self.id}, state="{self.state}", iftar_time="{self.iftar_time}")'


class Menu(Base):
    __tablename__ = 'menu items'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))   

    def __repr__(self):
        return f'Menu(id={self.id}, name={self.name})'