from random import random, randint, choice 

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Menu, Location, Restaurant, IftarTable

engine = create_engine('sqlite:///iftar.db')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

def make_locations():
    print("Deleting existing locations...")
    session.query(Location).delete()
    session.commit()

    print("Making locations...")

    locations = [
        Location(city='Los Angeles', state='California', restaurant_locations = 1, iftar_time = 1),
        Location(city='Chicago', state='Illinois', restaurant_locations = 2, iftar_time = 2),
        Location(city='New York', state='New York', restaurant_locations = 3, iftar_time = 3),
        Location(city='Miami', state='Florida', restaurant_locations = 4, iftar_time = 4),
        Location(city='Houston', state='Texas', restaurant_locations = 5, iftar_time = 5),
    ]

    session.add_all(locations)
    session.commit()

    return locations

def make_restaurant():
    print("Deleting existing restaurants...")
    session.query(Restaurant).delete()
    session.commit()

    print("Making Restaurant...")
    restaurants = [
        Restaurant(name='Halal Guys', city='Los Angeles', menu='gyro', location_id=1),
        Restaurant(name='Rumi\'s Kitchen', city='Los Angeles', menu='kebab', location_id=1),
        Restaurant(name='Pita Inn', city='Chicago', menu='shawarma', location_id=2),
        Restaurant(name='Naya Express', city='Chicago', menu='pita', location_id=2),
        Restaurant(name='Kabul Grill', city='New York', menu='burrito bowl', location_id=3),
        Restaurant(name='Taste of Persia', city='New York', menu='joojeh', location_id=3),
        Restaurant(name='Zaatar Mediterranean Cuisine', city='Miami', menu='hummus', location_id=4),
        Restaurant(name='Roaming Roosters', city='Miami', menu='Chicken Sandwich', location_id=4),
        Restaurant(name='Sabri Nihari', city='Houston', menu='Nihari', location_id=5),
        Restaurant(name='Akbar Restaurant', city='Houston', menu='Quesadilla', location_id=5)
    ]
    
    session.add_all(restaurants)
    session.commit()

    return restaurants

def make_iftartable():
    print("Deleting existing iftar tables...")
    session.query(IftarTable).delete()
    session.commit()

    print("Making iftar tables...")
    iftar_tables = [
        IftarTable(state='California', iftar_time='7:10 PM', location_id=1),
        IftarTable(state='Illinois', iftar_time='6:50 PM', location_id=2),
        IftarTable(state='New York', iftar_time='6:45 PM', location_id=3),
        IftarTable(state='Florida', iftar_time='7:30 PM', location_id=4),
        IftarTable(state='Texas', iftar_time='7:20 PM', location_id=5)
    ]
    
    session.add_all(iftar_tables)
    session.commit()

def make_menu():
    print("Deleting existing menu...")
    session.query(Menu).delete()
    session.commit()

    print("Making menu...")
    menu = [
        Menu(name='Lamb over rice', restaurant_id =1),
        Menu(name='Chicken over rice', restaurant_id =1),
        Menu(name='Combo over rice', restaurant_id =1),
        Menu(name='Kofta Kabob', restaurant_id =2),
        Menu(name='Shakshuka', restaurant_id =2),
        Menu(name='Kebsah', restaurant_id =2),
        Menu(name='Hummus', restaurant_id =3),
        Menu(name='Kibbeh', restaurant_id =3),
        Menu(name='Falafel Sandwich', restaurant_id =3),
        Menu(name='Beef Shawarma', restaurant_id =4),
        Menu(name='Chicken Shawarma', restaurant_id =4),
        Menu(name='Sujuk', restaurant_id =4),
        Menu(name='Spinach Sambo', restaurant_id =5),
        Menu(name='Kobideh Kabob', restaurant_id =5),
        Menu(name='Falafel', restaurant_id =5),
        Menu(name='Beef Koobideh', restaurant_id =6),
        Menu(name='Shishlik', restaurant_id =6),
        Menu(name='Gheyme', restaurant_id =6),
        Menu(name='Lebanese Bride', restaurant_id =7),
        Menu(name='Hot Halaby Honey', restaurant_id =7),
        Menu(name='Lahm Bi Ajeen', restaurant_id =7),
        Menu(name='Nashville Hot Chicken', restaurant_id =8),
        Menu(name='Honey Butter Chicken', restaurant_id =8),
        Menu(name='Honey Garlic Chicken', restaurant_id =8),
        Menu(name='Nihari', restaurant_id =9),
        Menu(name='Biryani', restaurant_id =9),
        Menu(name='Chaana Chaat', restaurant_id =9),
        Menu(name='Chicken Tikka Masla', restaurant_id =10),
        Menu(name='Chana Masala', restaurant_id =10),
        Menu(name='Malai Kofta', restaurant_id =10),
    ]

    session.add_all(menu)
    session.commit()

if __name__ == '__main__':
    make_locations()
    make_restaurant()
    make_iftartable()
    make_menu()