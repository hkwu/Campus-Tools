__author__ = 'Kelvin Wu'

from uwaterlooapi import UWaterlooAPI
import config

uw = UWaterlooAPI(api_key=config.super_secret_key)
infosesh = uw.infosessions()


# ====================================================
def sesh_getter(sesh):
    """takes a list of infosessions and prints the
    elements in groups of 5"""
    if len(sesh) >= 5:
        print "Here are the next 5 upcoming infosessions:\n", "-" * 20
        for infosession in sesh[0:5]:
            print """Employer: {}
Date: {}
Starts: {}
Ends: {}
Location: {}
Website: {}
Audience: {}
Programs: {}
Description: {}""".format(infosession['employer'], infosession['date'],
                          infosession['start_time'], infosession['end_time'],
                          infosession['location'], infosession['website'],
                          infosession['audience'], infosession['programs'],
                          infosession['description'])
            print "-" * 20
        import interface
        if len(sesh[5:]) >= 1:
            print "\nPress 'Y' to load more, or any other key to return.\n"
            if raw_input("> ").upper() == "Y":
                interface.scrn_clr()
                interface.CampusInfo().title()
                sesh_getter(sesh[5:])
            else:
                interface.scrn_clr()
                interface.CampusInfo().__str__()
                interface.CampusInfo().choice()
        else:
            print "\nPress any key to return.\n"
            raw_input("> ")
            interface.scrn_clr()
            interface.CampusInfo().__str__()
            interface.CampusInfo().choice()
    else:
        print "Here are the next {} upcoming infosessions:\n" \
            .format(len(sesh)), "-" * 20
        for infosession in sesh:
            print """Employer: {}
Date: {}
Starts: {}
Ends: {}
Location: {}
Website: {}
Audience: {}
Programs: {}
Description: {}""".format(infosession['employer'], infosession['date'],
                          infosession['start_time'], infosession['end_time'],
                          infosession['location'], infosession['website'],
                          infosession['audience'], infosession['programs'],
                          infosession['description'])
            print "-" * 20
        print "\nPress any key to return.\n"
        raw_input("> ")
        import interface
        interface.scrn_clr()
        interface.CampusInfo().__str__()
        interface.CampusInfo().choice()


def infosesh_user_enters():
    """wrapper for sesh_getter"""
    import interface
    interface.CampusInfo().title()
    if not infosesh:
        print "No one seems to be holding any infosessions right now!\n"
        print "Press any key to return.\n"
        raw_input("> ")
        interface.scrn_clr()
        interface.CampusInfo().__str__()
        interface.CampusInfo().choice()
    else:
        sesh_getter(infosesh)
# ====================================================