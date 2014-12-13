__author__ = 'Kelvin Wu'

from uwaterlooapi import UWaterlooAPI
import config

uw = UWaterlooAPI(api_key=config.super_secret_key)
weather = uw.current_weather()


# basic_weather_get() will extract basic information from weather
def basic_weather_get():
    print "Current Temperature (degrees): {}" \
        .format(weather['temperature_current_c'])
    print "Humidex: {}".format(weather['humidex_c'])
    print "Windchill: {}".format(weather['windchill_c'])
    print "24 Hour (High / Low): {} / {}" \
        .format(weather['temperature_24hr_max_c'],
                weather['temperature_24hr_min_c'])
    print "Precipitation (mm) (15 min / 1 hr / 24 hr): {} / {} / {}" \
        .format(weather['precipitation_15min_mm'],
                weather['precipitation_1hr_mm'],
                weather['precipitation_24hr_mm'])
    print "-" * 20, "\n"


# trivial_weather_get() will extract trivial information from weather
def trivial_weather_get():
    print "Station (Latitude / Longitude): {} / {}" \
        .format(weather['latitude'], weather['longitude'])
    print "Station Elevation: {} m".format(weather['elevation_m'])
    print "Relative Humidity: {} %".format(weather['relative_humidity_percent'])
    print "Dew Point: {}".format(weather['dew_point_c'])
    print "Wind (Speed / Direction): {} km/h / {} degrees" \
        .format(weather['wind_speed_kph'], weather['wind_direction_degrees'])
    print "Pressure (Amount / Trend): {} kPa / {}" \
        .format(weather['pressure_kpa'], weather['pressure_trend'])
    print "Incoming Shortwave Radiation: {} W/m^2" \
        .format(weather['incoming_shortwave_radiation_wm2'])
    print "-" * 20, "\n"


# basic_user_enters() is the basic I/O loop for basic weather
def basic_user_enters():
    import interface
    interface.CampusWeather().title()
    basic_weather_get()
    print "Press any key to return.\n"
    raw_input("> ")
    interface.scrn_clr()
    interface.CampusWeather().__str__()
    interface.CampusWeather().choice()


# trivial_user_enters() is the basic I/O loop for trivial weather
def trivial_user_enters():
    import interface
    interface.CampusWeather().title()
    trivial_weather_get()
    print "Press any key to return.\n"
    raw_input("> ")
    interface.scrn_clr()
    interface.CampusWeather().__str__()
    interface.CampusWeather().choice()