#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Base, User, Restaurant, Menu, IftarTable, Location

# if __name__ == 'main':

engine = create_engine('sqlite:///iftar.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

import ipdb; ipdb.set_trace()