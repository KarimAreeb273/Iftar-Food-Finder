from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import User, Location, Restaurant, IftarTable, Menu

from helpers import (create_location_table, create_restaurant_table, create_menu_table)


engine = create_engine('sqlite:///iftar.db')
session = sessionmaker(bind=engine)()

if __name__ == '__main__':
    print('''


  
  _    _       _       _   ______              _   ______ _           _           
 | |  | |     | |     | | |  ____|            | | |  ____(_)         | |          
 | |__| | __ _| | __ _| | | |__ ___   ___   __| | | |__   _ _ __   __| | ___ _ __ 
 |  __  |/ _` | |/ _` | | |  __/ _ \ / _ \ / _` | |  __| | | '_ \ / _` |/ _ \ '__|
 | |  | | (_| | | (_| | | | | | (_) | (_) | (_| | | |    | | | | | (_| |  __/ |   
 |_|  |_|\__,_|_|\__,_|_| |_|  \___/ \___/ \__,_| |_|    |_|_| |_|\__,_|\___|_|   
                                                                                        
_____________________________________________________________________________________      
                                                                                                                                                                                                                                                                                  
    ''')

    while True:
        full_name = input('''
    Mashallah, you made it through a whole day of fasting!
    You find your stomach grumbling as you approach the last hour before iftar. 
    You start thinking about where you're going to eat, but realize you don't 
    know ANY halal restaurants in your area. 

    Enter your NAME to embark on a journey to find the perfect iftar meal for you to satisfy those cravings (or press q to quit):
________________________________________________________________________________________________________

        ''')
        if full_name == "q":
            break
        else:
            print(f'''
           
    Salam {full_name}! I imagine you must be feeling extremely hungry by now.
    Don't worry.... you'll eat soon enough. Here are a list of cities with popular Halal options!''')

            locations = session.query(Location).all()
            create_location_table(locations)

            city = input('''
        
    Enter the city of your choice from the list above: 
        
        ''')
        
        state = input('''
        
    I know silly question but um... what state is that in again: 
        
        ''')
        
        location = session.query(Location).filter_by(city=city, state=state).first()
        if location is None:
            print(f"Sorry, we couldn't find a location matching {city}, {state}, please try again next time.")
            continue

        print ('''
        
    Perfect! We're almost there. Below are some awesome restaurants in the area. Any suit your interest?
       
        ''')
        restaurants = session.query(Restaurant).filter(Restaurant.city == city).all()
        create_restaurant_table(restaurants)

        iftar_time = session.query(IftarTable.iftar_time).filter(IftarTable.state == state).first()
        print(f"Your iftar time is: {iftar_time} almost there. SO SO SOON")
        find_iftar = input('''
        
        Would you like to move forward and choose a restaurant? I know, I know... so many options, It's a difficult decision (y/n): 
        
        ''')
        while find_iftar!= "y" or find_iftar!= "n":
            if find_iftar == "y":
                break
            elif find_iftar == "n":
                print("Thanks for using the Iftar Food Finder!")
                quit()
            else:
                find_iftar = input("Please enter y or n: ")
                

        restaurant_choices = input("Go ahead and select a restaurant ID from above: ")
        restaurant = session.query(Restaurant.name).filter(Restaurant.id == restaurant_choices).first()[0]

        restaurant_choice = session.query(Menu).filter(Menu.restaurant_id == restaurant_choices)
        create_menu_table(restaurant_choice)

        menu_choices = input("Great choice! Now you can choose a food item by selecting from a menu ID: ")
        menu_choice = session.query(Menu.name).filter(Menu.id == menu_choices).first()[0]
        print(menu_choice)

        print(f''' 

        WOW {menu_choice} might be the most delicious option for tonight, I wish I could have some with you! Share? Never mind.
        ''')

        leave_rating = input('''
        
        Since you just gobbled up that entire meal without sharing, would you like to leave a rating? (y/n): 
        
        ''')
        while leave_rating!= "y" or leave_rating!= "n":
            if leave_rating == "y":
                break
            elif leave_rating == "n":
                print('''
                
                Thank you for using the Iftar Food Finder! It was a pleasure helping you along the way. Please use our services again next time!
                
                ''')
                quit()
            else:
                leave_rating = input("Please enter y or n: ")
        
        rating = input("Please enter your rating out of 10: ")

        user = User(full_name=full_name, city=city, rating=rating, restaurant = restaurant, menu=menu_choice)
        session.add(user)
        session.commit()

        print(f"Thank you for using the Iftar Food Finder! It was a pleasure helping you on this journey. Thank you for your feedback and see you soon!")

        break
        
            







