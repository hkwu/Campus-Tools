__author__ = 'Kelvin Wu'

from uwaterlooapi import UWaterlooAPI
import config
uw = UWaterlooAPI(api_key=config.super_secret_key)


# ======================
# CAMPUS TUTORS
tutor_version = 1.01
tutors = uw.tutors()


class Tutor():
    def __init__(self, course_letter, course_number):
        self.course_letter = course_letter
        self.course_number = course_number

    def info_getter(self):
        for tutor_info in tutors:
            if tutor_info['subject'] == self.course_letter \
                    and tutor_info['catalog_number'] == self.course_number:
                print "Course: {0} {1} {2}\n# of Tutors: {3}\nContact: {4}" \
                    .format(tutor_info['subject'], tutor_info['catalog_number'],
                            tutor_info['title'], tutor_info['tutors_count'],
                            tutor_info['contact_url'])
                break
        else:
            print "Sorry, that course is not on the list."
# ======================


# ======================
# CAMPUS FOOD
food_version = 1.02
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


# The loop function
def menu_loop():
    avail_options = ['SEARCH FOR A MENU', 'RETURN']

    print "CAMPUS FOOD v{}\nCoded by {}".format(food_version, __author__)
    print "=" * 20, "\n"
    print "\n\nEnter your specifications."
    while continue_menu:
        for option in avail_options:
            print "{}: {}".format(avail_options.index(option) + 1, option)
        print ""
        user_choice = raw_input("> ")
        if user_choice == "1":
            user_location = raw_input("Which location? ").lower()
            user_day = raw_input("On what day? ").capitalize()
            user_meal = raw_input("For which meal? ").lower()
            Menu(user_location, user_meal, user_day).curr_menu()
        elif user_choice == "2":
            import interface
            interface.init_loop()
# ======================