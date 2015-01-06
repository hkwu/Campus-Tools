__author__ = 'Kelvin Wu'

import config


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
    from uwaterlooapi import UWaterlooAPI
    import interface
    interface.CampusInfo().title()
    uw = UWaterlooAPI(api_key=config.super_secret_key)
    infosesh = uw.infosessions()
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


# ====================================================
def goosewatch(goose_info):
    """prints the goosewatch information"""
    import dateutil.parser
    if len(goose_info) >= 5:
        print "The geese have taken over these locations:\n", "-" * 20
        for goose_location in goose_info[0:5]:
            parsed_date = dateutil.parser.parse(goose_location['updated'])
            print """Location: {}
Latitude: {}
Longitude: {}
Last Update: {}""".format(goose_location['location'],
                          goose_location['latitude'],
                          goose_location['longitude'],
                          parsed_date.strftime('%B %d, %Y'))
            print "-" * 20
        import interface
        if len(goose_info[5:]) >= 1:
            print "\nPress 'Y' to load more, or any other key to return.\n"
            if raw_input("> ").upper() == "Y":
                interface.scrn_clr()
                interface.CampusInfo().title()
                goosewatch(goose_info[5:])
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
        print "The geese have taken over these locations:\n", "-" * 20
        for goose_location in goose_info:
            parsed_date = dateutil.parser.parse(goose_location['updated'])
            print """Location: {}
Latitude: {}
Longitude: {}
Last Update: {}""".format(goose_location['location'],
                          goose_location['latitude'],
                          goose_location['longitude'],
                          parsed_date.strftime('%B %d, %Y'))
            print "-" * 20
        print "\nPress any key to return.\n"
        raw_input("> ")
        import interface
        interface.scrn_clr()
        interface.CampusInfo().__str__()
        interface.CampusInfo().choice()


# Sending a GET request and parsing the JSON response
# manually since the relevant function doesn't exist in
# the UWaterlooAPI module
def goosewatch_user_enters():
    """wrapper for goosewatch"""
    import interface
    import requests
    resp = requests.get("https://api.uwaterloo.ca/v2/resources/goosewatch.json",
                        params={'key':config.super_secret_key})
    interface.CampusInfo().title()
    gw = resp.json()['data']
    if not gw:
        print "The campus is currently safe from geese. Check again later!\n"
        print "Press any key to return.\n"
        raw_input("> ")
        interface.scrn_clr()
        interface.CampusInfo().__str__()
        interface.CampusInfo().choice()
    else:
        goosewatch(gw)
# ====================================================