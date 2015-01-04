__author__ = 'Kelvin Wu'

from uwaterlooapi import UWaterlooAPI
import config

uw = UWaterlooAPI(api_key=config.super_secret_key)


# ====================================================
def curr_menu(location, meal, day):
    """curr_menu() outputs the daily menu"""
    menu = uw.menu()
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
        print "\nSorry, we couldn't find that outlet's menu!\n"


def meal_getter(meal, daily_menu, location, day):
    """outputs the dishes for the meal type"""
    if meal in ["lunch", "dinner"]:
        avail_dishes = daily_menu[meal]
        print "\nHere is the {} {} menu for {}:" \
            .format(day, meal, location)
        print "-" * 20
        for dish in avail_dishes:
            print "Dish: {}\nType: {}\nID: {}".format(dish['product_name'],
                                                      dish['diet_type'],
                                                      dish['product_id'])
            print "-" * 20
        print ""
    else:
        print "\nSorry, we don't serve that here!\n"


def menu_user_enters():
    """gets the input for curr_menu"""
    import interface
    interface.CampusFood().title()
    print "Enter your specifications.\n"
    user_location = raw_input("Location: ").lower()
    user_day = raw_input("Day: ").capitalize()
    user_meal = raw_input("Meal: ").lower()
    curr_menu(user_location, user_meal, user_day)
    print "Press any key to return.\n"
    raw_input("> ")
    interface.scrn_clr()
    interface.CampusFood().__str__()
    interface.CampusFood().choice()
# ====================================================


# ====================================================
def open_outlets():
    """determines which outlets are open at the
    current time"""
    locations = uw.locations()
    open_now = []
    for outlet in locations:
        if outlet['is_open_now']:
            open_now.append(outlet['outlet_name'] +
                            " ({})".format(outlet['building']))
    outlet_printer(open_now)


def outlet_printer(lst_of_outlets):
    """takes a list of outlets and prints the
    list, if non-empty"""
    if lst_of_outlets:
        print "These places are open right now:\n", "-" * 20
        for outlet in lst_of_outlets:
            if u"\u2019" in outlet:
                print u"{}: {}\n".format(lst_of_outlets.index(outlet) + 1,
                                         outlet.replace(u"\u2019", "'"))
            else:
                print u"{}: {}".format(lst_of_outlets.index(outlet) + 1,
                                       outlet)
        print "-" * 20, "\n"
    else:
        print "Sorry, it seems like no one's open right now!\n"


def open_user_enters():
    """the wrapper for open_outlets"""
    import interface
    interface.CampusFood().title()
    open_outlets()
    print "Press any key to return.\n"
    raw_input("> ")
    interface.scrn_clr()
    interface.CampusFood().__str__()
    interface.CampusFood().choice()
# ====================================================


# ====================================================
def nutrition_info(prod_id):
    """gets the nutrition info for the given product ID"""
    product = uw.products(prod_id)
    if product:
        print "\nNutrition Information for {}\n{}\n" \
            .format(product['product_name'],
                    product['diet_type']), "-" * 20
        print """Serving Size: {}
Calories: {}
Total Fat (g / %): {} / {}
  Saturated Fat: {} / {}
  Trans Fat: {} / {}
Cholesterol (mg): {}
Sodium (mg / %): {} / {}
Carbohydrates (g / %): {} / {}
  Fibre: {} / {}
  Sugar (g): {}
Protein (g): {}""" \
            .format(product['serving_size'], product['calories'],
                    product['total_fat_g'], product['total_fat_percent'],
                    product['fat_saturated_g'], product['fat_saturated_percent'],
                    product['fat_trans_g'], product['fat_trans_percent'],
                    product['cholesterol_mg'], product['sodium_mg'],
                    product['sodium_percent'], product['carbo_g'],
                    product['carbo_percent'], product['carbo_fibre_g'],
                    product['carbo_fibre_percent'], product['carbo_sugars_g'],
                    product['protein_g'])
        print "-" * 20
        print """Vitamin A (%): {}
Vitamin C (%): {}
Calcium (%): {}
Iron (%): {}
Micronutrients: {}""" \
            .format(product['vitamin_a_percent'], product['vitamin_c_percent'],
                    product['calcium_percent'], product['iron_percent'],
                    product['micro_nutrients'])
        print "-" * 20, "\nIngredients: {}\n".format(product['ingredients']), \
            "-" * 20
        print "Consumption Tips: {}\n".format(product['tips']), "-" * 20, "\n"
    else:
        print "\nSorry, we couldn't find that dish!\n"


def nutrition_user_enters():
    """gets the product ID for nutrition_info"""
    import interface
    interface.CampusFood().title()
    nutrition_info(int(raw_input("Enter your product ID: ")))
    print "Press any key to return.\n"
    raw_input("> ")
    interface.scrn_clr()
    interface.CampusFood().__str__()
    interface.CampusFood().choice()
# ====================================================