__author__ = 'Kelvin Wu'

from uwaterlooapi import UWaterlooAPI
import config

uw = UWaterlooAPI(api_key=config.super_secret_key)
weather = uw.current_weather()


# ====================================================
def basic_weather_get():
    """extract basic information from weather"""
    print ("Current Temperature (degrees): {}\n"
           "Humidex: {}\n"
           "Windchill: {}\n"
           "24 Hour (High / Low): {} / {}\n"
           "Precipitation (mm) (15 min / 1 hr / 24 hr): {} / {} / {}\n"
           "--------------------\n") \
        .format(weather['temperature_current_c'], weather['humidex_c'],
                weather['windchill_c'], weather['temperature_24hr_max_c'],
                weather['temperature_24hr_min_c'], weather['precipitation_15min_mm'],
                weather['precipitation_1hr_mm'], weather['precipitation_24hr_mm'])


def basic_user_enters():
    """the interface for basic weather"""
    import interface
    interface.CampusWeather().title()
    basic_weather_get()
    print "Press any key to return.\n"
    raw_input("> ")
    interface.scrn_clr()
    interface.CampusWeather().__str__()
    interface.CampusWeather().choice()
# ====================================================


# ====================================================
def trivial_weather_get():
    """extract trivial information from weather"""
    print ("Station (Latitude / Longitude): {} / {}\n"
           "Station Elevation: {} m\n"
           "Relative Humidity: {} %\n"
           "Dew Point: {}\n"
           "Wind (Speed / Direction): {} km/h / {} degrees\n"
           "Pressure (Amount / Trend): {} kPa / {}\n"
           "Incoming Shortwave Radiation: {} W/m^2\n"
           "--------------------\n") \
        .format(weather['latitude'], weather['longitude'],
                weather['elevation_m'], weather['relative_humidity_percent'],
                weather['dew_point_c'], weather['wind_speed_kph'],
                weather['wind_direction_degrees'], weather['pressure_kpa'],
                weather['pressure_trend'], weather['incoming_shortwave_radiation_wm2'])


def trivial_user_enters():
    """the interface for trivial weather"""
    import interface
    interface.CampusWeather().title()
    trivial_weather_get()
    print "Press any key to return.\n"
    raw_input("> ")
    interface.scrn_clr()
    interface.CampusWeather().__str__()
    interface.CampusWeather().choice()
# ====================================================