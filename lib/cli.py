from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import User, Location, Restaurant, IftarTable, Menu

from helpers import (create_location_table, create_restaurant_table, create_menu_table)


engine = create_engine('sqlite:///iftar.db')
session = sessionmaker(bind=engine)()

if __name__ == '__main__':
    print('Welcome to the Iftar Food Finder')

    while True:
        full_name = input("Enter your full name (or press q to quit or to continue): ")
        if full_name == "q":
            break
        else:
            print('These are the possible options for Cities:')
            locations = session.query(Location).all()
            create_location_table(locations)

            city = input("Enter your city: ")

        state = input("Enter the state your city is in: ")
        
        location = session.query(Location).filter_by(city=city, state=state).first()
        if location is None:
            print(f"Sorry, we couldn't find a location matching {city}, {state}, please try again next time.")
            continue

        print ("Here are the halal restaurants in your city:")
        restaurants = session.query(Restaurant).filter(Restaurant.city == city).all()
        create_restaurant_table(restaurants)

        iftar_time = session.query(IftarTable.iftar_time).filter(IftarTable.state == state).first()
        print(f"Your iftar time is: {iftar_time}")
        find_iftar = input("Would you like to find your iftar? (y/n): ")
        while find_iftar!= "y" or find_iftar!= "n":
            if find_iftar == "y":
                break
            elif find_iftar == "n":
                print("Thanks for using the Iftar Food Finder!")
                quit()
            else:
                find_iftar = input("Please enter y or n: ")
                

        restaurant_choices = input("Choose a restaurant ID: ")
        restaurant = session.query(Restaurant.name).filter(Restaurant.id == restaurant_choices).first()[0]

        restaurant_choice = session.query(Menu).filter(Menu.restaurant_id == restaurant_choices)
        create_menu_table(restaurant_choice)

        menu_choices = input("Choose a menu ID: ")
        menu_choice = session.query(Menu.name).filter(Menu.id == menu_choices).first()[0]
        print(menu_choice)

        print(f"Please enjoy your {menu_choice}!")

        leave_rating = input("Would you like to leave the rating? (y/n): ")
        while leave_rating!= "y" or leave_rating!= "n":
            if leave_rating == "y":
                break
            elif leave_rating == "n":
                print("Thank you for using the Iftar Food Finder! Please use our services again next time!")
                quit()
            else:
                leave_rating = input("Please enter y or n: ")
        
        rating = input("Please enter your rating out of 10: ")

        user = User(full_name=full_name, city=city, rating=rating, restaurant = restaurant, menu=menu_choice)
        session.add(user)
        session.commit()

        print(f"Thank you for using the Iftar Food Finder! Thank you for your feedback and see you soon!")






