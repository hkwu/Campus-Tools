__author__ = 'Kelvin Wu'

from uwaterlooapi import UWaterlooAPI
import config
import subprocess as sp

uw = UWaterlooAPI(api_key=config.super_secret_key)
menu = uw.menu()


# curr_menu() outputs the daily menu
def curr_menu(location, meal, day):
    for outlet in menu['outlets']:
        if outlet['outlet_name'].lower() == location:
            outlet_name = outlet['outlet_name']
            outlet_menus = outlet['menu']
            for daily_menus in outlet_menus:
                if daily_menus['day'] == day:
                    meal_getter(meal, daily_menus['meals'], outlet_name, day)
                    break
            else:
                print "\nSorry, there is no menu available for that day!\n"
            break
    else:
        print "\nSorry, we couldn't find that outlet!\n"


# meal_getter() outputs the dishes for the meal type
def meal_getter(meal, daily_menu, location, day):
    if meal in ["lunch", "dinner"]:
        avail_dishes = daily_menu[meal]
        print "\nHere is the {} {} menu for {}:" \
            .format(day, meal, location)
        print "-" * 20
        for dish in avail_dishes:
            print "Dish: {}\nType: {}".format(dish['product_name'],
                                              dish['diet_type'])
            print "-" * 20
        print ""
    else:
        print "\nSorry, we don't serve that here!\n"


# user_enters() is the basic I/O loop
def user_enters():
    user_location = raw_input("Which location? ").lower()
    user_day = raw_input("On what day? ").capitalize()
    user_meal = raw_input("For which meal? ").lower()
    curr_menu(user_location, user_meal, user_day)
    print "Press 'B' to return to the menu.\n"
    while not raw_input("> ").upper() == "B":
        scrn_clr = sp.call('cls', shell=True)
        print "Press 'B' to return to the menu.\n"
    else:
        import interface
        scrn_clr = sp.call('cls', shell=True)
        interface.CampusFood().__str__()
        interface.CampusFood().choice()