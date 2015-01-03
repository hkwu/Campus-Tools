__author__ = 'Kelvin Wu'

import config


# ====================================================
def sesh_getter():
    """takes a list of infosessions and prints the
    elements in groups of 5"""
    from uwaterlooapi import UWaterlooAPI

    uw = UWaterlooAPI(api_key=config.super_secret_key)
    infosesh = uw.infosessions()

    text = ''
    for infosession in infosesh:
        text += ("Employer: {}\n"
                 "Date: {}\n"
                 "Starts: {}\n"
                 "Ends: {}\n"
                 "Location: {}\n"
                 "Website: {}\n"
                 "Audience: {}\n"
                 "Programs: {}\n"
                 "Description: {}\n"
                 "--------------------\n") \
            .format(infosession['employer'], infosession['date'],
                    infosession['start_time'], infosession['end_time'],
                    infosession['location'], infosession['website'],
                    infosession['audience'], infosession['programs'],
                    infosession['description'])
    return text
# ====================================================


# ====================================================
def goosewatch():
    """prints the goosewatch information"""
    import dateutil.parser
    import requests

    resp = requests.get("https://api.uwaterloo.ca/v2/resources/goosewatch.json",
                        params={'key':config.super_secret_key})
    gw = resp.json()['data']

    text = ''
    for goose_location in gw:
        parsed_date = dateutil.parser.parse(goose_location['updated'])
        text += ("Location: {}\n"
                 "Latitude: {}\n"
                 "Longitude: {}\n"
                 "Last Update: {}\n"
                 "--------------------\n") \
            .format(goose_location['location'],
                    goose_location['latitude'],
                    goose_location['longitude'],
                    parsed_date.strftime('%B %d, %Y'))
    return text
# ====================================================