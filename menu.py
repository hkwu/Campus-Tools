__author__ = 'Kelvin Wu'
version = 1.02

from uwaterlooapi import UWaterlooAPI
import config

uw = UWaterlooAPI(api_key=config.super_secret_key)
menu = uw.menu()


class Menu():
    def __init__(self, location, meal, day):
        self.location = location
        self.meal = meal
        self.day = day

    # curr_menu() outputs the daily menu
    def curr_menu(self):
        for outlet in menu['outlets']:
            if outlet['outlet_name'].lower() == self.location:
                outlet_name = outlet['outlet_name']
                outlet_menus = outlet['menu']
                for daily_menus in outlet_menus:
                    if daily_menus['day'] == self.day:
                        self.meal_getter(daily_menus['meals'], outlet_name)
                        break
                else:
                    print "\nSorry, there is no menu available for that day!\n"
                break
        else:
            print "\nSorry, we couldn't find that outlet!\n"

    # meal_getter() outputs the dishes for the meal type
    def meal_getter(self, meals, location):
        if self.meal in ["lunch", "dinner"]:
            avail_dishes = meals[self.meal]
            print "\nHere is the {} {} menu for {}:" \
                .format(self.day, self.meal, location)
            print "-" * 20
            for dish in avail_dishes:
                print "Dish: {}\nType: {}".format(dish['product_name'],
                                                  dish['diet_type'])
                print "-" * 20
            print ""
        else:
            print "\nSorry, we don't serve that here!\n"


print "University of Waterloo Menu Tool v{}\nCoded by {}" \
    .format(version, __author__)
print "=" * 20, "\n\nEnter your specifications."
while True:
    user_location = raw_input("Which location? ").lower()
    user_day = raw_input("On what day? ").capitalize()
    user_meal = raw_input("For which meal? ").lower()
    Menu(user_location, user_meal, user_day).curr_menu()