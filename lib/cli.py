from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import User, Location, Restaurant, IftarTable, Menu

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
        else:
            print('These are the possible options for Cities:')
            locations = session.query(Location).all()
            create_location_table(locations)

            city = input("Enter your city: ")
            user = User(full_name=full_name, city=city)
            users.append(user)
            session.add_all(users)
            session.commit()

        state = input("Enter the state your city is in: ")
        
        location = session.query(Location).filter_by(city=city, state=state).first()
        if location is None:
            print(f"Sorry, we couldn't find a location matching {city}, {state}")
            continue

        print ("Here are the halal restaurants in your city:")
        restaurants = session.query(Restaurant).filter(Restaurant.city == city).all()
        create_restaurant_table(restaurants)

        iftar_time = session.query(IftarTable.iftar_time).filter(IftarTable.state == state).first()
        print(f"Your iftar time is: {iftar_time} Enjoy your dinner!")
        find_iftar = input("Would you like to find your iftar? (y/n): ")
        while find_iftar!= "y" or find_iftar!= "n":
            if find_iftar == "y":
                break
            elif find_iftar == "n":
                print("Thanks for visiting!")
                quit()
            else:
                find_iftar = input("Please enter y or n: ")
                

        restaurant_choices = input("Choose a restaurant ID: ")
        restaurant_choice = session.query(Menu).filter(Menu.restaurant_id == restaurant_choices)
        create_menu_table(restaurant_choice)


