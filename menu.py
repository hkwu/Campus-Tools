__author__ = 'Kelvin Wu'

from uwaterlooapi import UWaterlooAPI

uw = UWaterlooAPI(api_key='523a61d18c31481685e8957becd8727f')
menu = uw.menu()

class Menu():
    def __init__(self, location, meal, day):
        self.location = location
        self.meal = meal
        self.day = day

    # curr_menu() outputs the daily menu
    def curr_menu(self):
        for outlet in menu['outlets']:
            if outlet['outlet_name'] == self.location:
                outlet_menus = outlet['menu']
                for daily_menus in outlet_menus:
                    if daily_menus['day'] == self.day:
                        self.meal_getter(daily_menus['meals'])
            else:
                pass

    # meal_getter() outputs the dishes for the meal type
    def meal_getter(self, meals):
        avail_dishes = meals[self.meal]
        for dish in avail_dishes:
            print "Dish: {}\nType: {}".format(dish['product_name'],
                                              dish['diet_type'])

Menu('REVelation', 'dinner', 'Monday').curr_menu()

while True:
    user_location = raw_input("Enter a location.\n")
    user_meal = raw_input("Enter a meal.\n")
    user_day = raw_input("Enter the day.\n")
    Menu(user_location, user_meal, user_day).curr_menu()