__author__ = 'Kelvin Wu'

import subprocess as sp
import sys

version = 1.0


# Base menu class
class Menu(object):
    def __init__(self, menu_name, vrsion, *args):
        self.menu_name = menu_name
        self.version = vrsion
        self.args = args

    def __str__(self):
        avail_options = []
        for option in self.args:
            avail_options.append(option)
        print "{} v{}\nCoded by {}"\
            .format(self.menu_name, self.version, __author__)
        print "=" * 20, "\n"
        for option in avail_options:
            print "{}: {}".format(avail_options.index(option) + 1, option)
        print ""


# The initial menu screen
class TopMenu(Menu):
    def __init__(self):
        super(TopMenu, self).__init__("CAMPUS TOOLS", 1.0,
                                      "CAMPUS TUTORS", "CAMPUS FOOD",
                                      "EXIT")

    def choice(self):
        usr_input = raw_input("> ")
        while usr_input not in ["3", "EXIT"]:
            if usr_input in ["1", "CAMPUS TUTORS"]:
                import tutors
                pass
            elif usr_input in ["2", "CAMPUS FOOD"]:
                scrn_clr = sp.call('cls', shell=True)
                CampusFood().__str__()
                CampusFood().choice()
            else:
                scrn_clr = sp.call('cls', shell=True)
                TopMenu().__str__()
                return TopMenu().choice()
        else:
            scrn_clr = sp.call('cls', shell=True)
            sys.exit()


# The Campus Tutors menu
class CampusTutors(Menu):
    def __init__(self):
        super(CampusTutors, self).__init__("CAMPUS TUTORS", 1.01,
                                           "SEARCH", "EXIT")


# The Campus Food menu
class CampusFood(Menu):
    def __init__(self):
        super(CampusFood, self).__init__("CAMPUS FOOD", 1.02,
                                         "SEARCH FOR MENUS", "EXIT")

    def choice(self):
        usr_input = raw_input("> ")
        while usr_input not in ["2", "EXIT"]:
            if usr_input in ["1", "SEARCH FOR MENUS"]:
                scrn_clr = sp.call('cls', shell=True)
                import menu
                menu.user_enters()
            else:
                scrn_clr = sp.call('cls', shell=True)
                CampusFood().__str__()
                CampusFood().choice()
        else:
            scrn_clr = sp.call('cls', shell=True)
            TopMenu().__str__()
            TopMenu().choice()

# Initializing the interface
scrn_clr = sp.call('cls', shell=True)
TopMenu().__str__()
TopMenu().choice()