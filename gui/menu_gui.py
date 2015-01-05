__author__ = 'Kelvin Wu'

from uwaterlooapi import UWaterlooAPI
import config

uw = UWaterlooAPI(api_key=config.super_secret_key)


# ====================================================
def curr_menu(location, meal, day):
    """curr_menu() outputs the daily menu"""
    menu = uw.menu()
    for outlet in menu['outlets']:
        if outlet['outlet_name'] == location:
            outlet_menus = outlet['menu']
            for daily_menus in outlet_menus:
                if daily_menus['day'] == day:
                    return meal_getter(meal, daily_menus['meals'])
            else:
                return 'none_day'
    else:
        return False


def meal_getter(meal, daily_menu):
    """outputs the dishes for the meal type"""
    if meal in ["lunch", "dinner"]:
        avail_dishes = daily_menu[meal]
        text = ''
        for dish in avail_dishes:
            text += ("Dish: {}\n"
                     "Type: {}\n"
                     "ID: {}\n"
                     "--------------------\n") \
                .format(dish['product_name'],
                        dish['diet_type'],
                        dish['product_id'])
        return text
    else:
        return 'none_meal_type'
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
    return outlet_printer(open_now)


def outlet_printer(lst_of_outlets):
    """takes a list of outlets and returns the formatted
    list, if non-empty"""
    if lst_of_outlets:
        text = ''
        for outlet in lst_of_outlets:
            text += u"{}: {}\n".format(lst_of_outlets.index(outlet) + 1,
                                       outlet)
        return text
    else:
        return False
# ====================================================


# ====================================================
def nutrition_info(prod_id):
    """gets the nutrition info for the given product ID"""
    product = uw.products(prod_id)
    if product:
        return ("Nutrition Information for {}\n{}\n"
                "--------------------\n"
                "Serving Size: {}\n"
                "Calories: {}\n"
                "Total Fat (g / %): {} / {}\n"
                "  Saturated Fat: {} / {}\n"
                "  Trans Fat: {} / {}\n"
                "Cholesterol (mg): {}\n"
                "Sodium (mg / %): {} / {}\n"
                "Carbohydrates (g / %): {} / {}\n"
                "  Fibre: {} / {}\n"
                "  Sugar (g): {}\n"
                "Protein (g): {}\n"
                "--------------------\n"
                "Vitamin A (%): {}\n"
                "Vitamin C (%): {}\n"
                "Calcium (%): {}\n"
                "Iron (%): {}\n"
                "Micronutrients: {}\n"
                "--------------------\n"
                "Ingredients: {}\n"
                "--------------------\n"
                "Consumption Tips: {}\n"
                "--------------------") \
            .format(product['product_name'], product['diet_type'],
                    product['serving_size'], product['calories'],
                    product['total_fat_g'], product['total_fat_percent'],
                    product['fat_saturated_g'], product['fat_saturated_percent'],
                    product['fat_trans_g'], product['fat_trans_percent'],
                    product['cholesterol_mg'], product['sodium_mg'],
                    product['sodium_percent'], product['carbo_g'],
                    product['carbo_percent'], product['carbo_fibre_g'],
                    product['carbo_fibre_percent'], product['carbo_sugars_g'],
                    product['protein_g'], product['vitamin_a_percent'],
                    product['vitamin_c_percent'], product['calcium_percent'],
                    product['iron_percent'], product['micro_nutrients'],
                    product['ingredients'], product['tips'])
    else:
        return False
# ====================================================