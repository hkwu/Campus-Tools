__author__ = 'Kelvin Wu'

import os
import sys


def scrn_clr():
    """Screen clear function"""
    os.system('cls' if os.name == 'nt' else 'clear')


class Menu(object):
    """Base menu class"""
    def __init__(self, menu_name, *args):
        self.menu_name = menu_name
        self.args = args

    def __str__(self):
        avail_options = []
        for option in self.args:
            avail_options.append(option)
        print "{} by {}" \
            .format(self.menu_name,  __author__)
        print "=" * 20, "\n"
        for option in avail_options:
            print "{}: {}".format(avail_options.index(option) + 1, option)
        print ""

    def title(self):
        print "{} by {}" \
            .format(self.menu_name, __author__)
        print "=" * 20, "\n"


class TopMenu(Menu):
    """Base menu class"""
    def __init__(self):
        super(TopMenu, self).__init__("CAMPUS TOOLS", "CAMPUS TUTORS",
                                      "CAMPUS FOOD", "CAMPUS WEATHER",
                                      "CAMPUS INFO", "EXIT")

    def choice(self):
        usr_input = raw_input("> ").upper()
        while usr_input not in ["5", "EXIT"]:
            if usr_input in ["1", "CAMPUS TUTORS"]:
                scrn_clr()
                CampusTutors().__str__()
                CampusTutors().choice()
            elif usr_input in ["2", "CAMPUS FOOD"]:
                scrn_clr()
                CampusFood().__str__()
                CampusFood().choice()
            elif usr_input in ["3", "CAMPUS WEATHER"]:
                scrn_clr()
                CampusWeather().__str__()
                CampusWeather().choice()
            elif usr_input in ["4", "CAMPUS INFO"]:
                scrn_clr()
                CampusInfo().__str__()
                CampusInfo().choice()
            else:
                scrn_clr()
                TopMenu().__str__()
                TopMenu().choice()
        else:
            scrn_clr()
            sys.exit()


class CampusTutors(Menu):
    """The Campus Tutors menu"""
    def __init__(self):
        super(CampusTutors, self).__init__("CAMPUS TUTORS",
                                           "SEARCH FOR TUTORS", "RETURN")

    def choice(self):
        usr_input = raw_input("> ").upper()
        while usr_input not in ["2", "RETURN"]:
            if usr_input in ["1", "SEARCH FOR TUTORS"]:
                scrn_clr()
                import tutors
                tutors.user_enters()
            else:
                scrn_clr()
                CampusTutors().__str__()
                CampusTutors().choice()
        else:
            scrn_clr()
            TopMenu().__str__()
            TopMenu().choice()


class CampusFood(Menu):
    """The Campus Food menu"""
    def __init__(self):
        super(CampusFood, self).__init__("CAMPUS FOOD", "WHAT'S OPEN?",
                                         "SEARCH FOR MENUS", "NUTRITION INFO",
                                         "RETURN")

    def choice(self):
        usr_input = raw_input("> ").upper()
        while usr_input not in ["4", "RETURN"]:
            if usr_input in ["1", "WHAT'S OPEN?"]:
                scrn_clr()
                import menu
                menu.open_user_enters()
            elif usr_input in ["2", "SEARCH FOR MENUS"]:
                scrn_clr()
                import menu
                menu.menu_user_enters()
            elif usr_input in ["3", "NUTRITION INFO"]:
                scrn_clr()
                import menu
                menu.nutrition_user_enters()
            else:
                scrn_clr()
                CampusFood().__str__()
                CampusFood().choice()
        else:
            scrn_clr()
            TopMenu().__str__()
            TopMenu().choice()


class CampusWeather(Menu):
    """The Campus Weather menu"""
    def __init__(self):
        super(CampusWeather, self).__init__("CAMPUS WEATHER", "BASIC WEATHER",
                                            "TRIVIAL WEATHER", "RETURN")

    def choice(self):
        usr_input = raw_input("> ").upper()
        while usr_input not in ["3", "RETURN"]:
            if usr_input in ["1", "BASIC WEATHER"]:
                scrn_clr()
                import weather
                weather.basic_user_enters()
            elif usr_input in ["2", "TRIVIAL WEATHER"]:
                scrn_clr()
                import weather
                weather.trivial_user_enters()
            else:
                scrn_clr()
                CampusWeather().__str__()
                CampusWeather().choice()
        else:
            scrn_clr()
            TopMenu().__str__()
            TopMenu().choice()


class CampusInfo(Menu):
    """The Campus Info menu"""
    def __init__(self):
        super(CampusInfo, self).__init__("CAMPUS INFO",
                                         "EMPLOYER INFOSESSIONS", "RETURN")

    def choice(self):
        usr_input = raw_input("> ").upper()
        while usr_input not in ["2", "RETURN"]:
            if usr_input in ["1", "EMPLOYER INFOSESSIONS"]:
                scrn_clr()
                import info
                info.infosesh_user_enters()
            else:
                scrn_clr()
                CampusInfo().__str__()
                CampusInfo().choice()
        else:
            scrn_clr()
            TopMenu().__str__()
            TopMenu().choice()

# Initializing the interface
if __name__ == '__main__':
    scrn_clr()
    TopMenu().__str__()
    TopMenu().choice()