from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import User, Location, Restaurant, IftarTable

from helpers import (create_location_table, create_restaurant_table, create_menu_table)


engine = create_engine('sqlite:///iftar.db')
session = sessionmaker(bind=engine)()

if __name__ == '__main__':
    print('Welcome to the Iftar Food Finder')

    users = []
    while True:
        full_name = input("Enter your full name (or press q to quit or to continue): ")
        if full_name == "q":
            break

        print('These are the possible options for Cities:')
        locations = session.query(Location).all()
        create_location_table(locations)
        city = input("Enter your city: ")
        state = input("Enter the state your city is in: ")
        
        location = session.query(Location).filter_by(city=city, state=state).first()
        if location is None:
            print(f"Sorry, we couldn't find a location matching {city}, {state}")
            continue

        session.add_all(users)
        session.commit()


        print ("Here are the halal restaurants in your city:")
        restaurants = session.query(Restaurant).filter(Restaurant.city == city).all()
        create_restaurant_table(restaurants)

        restaurant_choices = input("Choose a restaurant: ")
        restaurant_choice = session.query(Restaurant.menu).filter(Restaurant.name == restaurant_choices).first()
        create_menu_table(restaurants)
        
        # restaurant_choice = session.query(Restaurant).join(Location).filter_by(city=city, state=state, name=restaurant_choices).first()


        # if restaurant_choice is None:
        #     print(f"Sorry, we couldn't find a restaurant matching {restaurant_choices}")
        #     continue

        # menu_items = session.query(Restaurant.menu).filter_by(name=restaurant_choices).first()
        # create_menu_table(menu_items)


        iftar_time = session.query(IftarTable.iftar_time).filter(IftarTable.state == state).first()
        print(f"Your iftar time is: {iftar_time} Enjoy your dinner!")

