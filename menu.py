__author__ = 'Kelvin Wu'
version = 1.01

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
                        print "\nHere is the {} {} menu for {}:" \
                            .format(self.day, self.meal, self.location)
                        print "-" * 20
                        self.meal_getter(daily_menus['meals'])
                        break
                break
        else:
            print "Sorry, that outlet has no menu available this week!"

    # meal_getter() outputs the dishes for the meal type
    def meal_getter(self, meals):
        avail_dishes = meals[self.meal]
        for dish in avail_dishes:
            print "Dish: {}\nType: {}".format(dish['product_name'],
                                              dish['diet_type'])
            print "-" * 20
        print ""


print "University of Waterloo Menu Tool v{}\nCoded by {}" \
    .format(version, __author__)
print "=" * 20

fs_outlets = ["Bon Appetit", "Festival Fare", "Mudie'S", "Pas Lounge",
              "Pastry Plus", "Revelation"]
avail_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
avail_meals = ["lunch", "dinner"]

while True:
    user_location = raw_input("Which location? ").title()
    while user_location not in fs_outlets:
        print "Sorry, we couldn't find that outlet!"
        user_location = raw_input("Which location? ").title()
    else:
        if user_location == "Revelation":
            user_location = "REVelation"
        elif user_location == "Mudie'S":
            user_location = "Mudie's"
        elif user_location == "Pas Lounge":
            user_location = "PAS Lounge"
        user_day = raw_input("On what day? ").capitalize()
        while user_day not in avail_days:
            print "Sorry, there are no menus for that day!"
            user_day = raw_input("On what day? ").capitalize()
        else:
            user_meal = raw_input("What meal? ").lower()
            while user_meal not in avail_meals:
                print "Sorry, we don't serve that on our menu!"
                user_meal = raw_input("What meal? ").lower()
            else:
                Menu(user_location, user_meal, user_day).curr_menu()