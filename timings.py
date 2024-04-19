import pytz 
import datetime
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

def get_timezone(place_name):
    # Initialize a geocoder
    geolocator = Nominatim(user_agent="timezone_locator")

    # Use the geocoder to obtain the location information (including latitude and longitude)
    location = geolocator.geocode(place_name)

    if location:
        # Extract latitude and longitude
        latitude = location.latitude
        longitude = location.longitude

        # Initialize the TimezoneFinder
        tz_finder = TimezoneFinder()

        # Use the library to find the time zone based on coordinates
        timezone_str = tz_finder.timezone_at(lng=longitude, lat=latitude)

        if timezone_str:
            return timezone_str
    else:
        return "Time zone not found."

def get_time(timezone_name):
    try:
        # Get the current time in the specified time zone
        tz = pytz.timezone(timezone_name)
        local_time = datetime.datetime.now(tz)
        str_time = local_time.strftime("%I:%M %p")
        return str_time
    except pytz.exceptions.UnknownTimeZoneError:
        return "Time zone not found."
    
    

