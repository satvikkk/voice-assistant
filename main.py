import re
import datetime
from speak import say
from listen import takeCommand

# api_key = AIzaSyCtDdUyJtt8KkJYbg-PYLofRbqMNi2hQ0M
OPENWEATHERMAP_API_KEY = "8c4a2e2abfe6e2204f3a5d31565a5178"

if __name__ == "__main__":
    while True:
        query = takeCommand()
        if "hello" in query or "hi" in query or "hey" in query or "wake up" in query:
            from greeting import greetMe
            greetMe()

            while True:
                query = takeCommand()
                if ("thank you" in query) or ("bye" in query) or ("take a break" in query):
                    say("Okay Sir! You can call me anytime.")
                    exit()

                elif "google" in query:
                    from websearch import searchGoogle
                    searchGoogle(query)
                    # searchGoogle(query, api_key, search_engine_id)

                elif "youtube" in query:
                    from websearch import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from websearch import searchWikipedia
                    searchWikipedia(query)

                elif ("weather" in query) or ("temparature" in query):
                    import weather
                    # Using RE to extract the city name from the query
                    city = re.search(r"(in|of|for) ([\w\s]+)", query, re.IGNORECASE)

                    # If we find a city's name in the query, we will use that otherwise we will get the user's location through his/her IP Address and get the weather for that location.
                    if city:
                        city = city[2] # Captures a sequence of alphabetic characters, which is expected to be the city name. The first [1] group is Prepositions (in, for, etc.)
                        weather_info = weather.get_weather(city, OPENWEATHERMAP_API_KEY)  # Using the function from weather.py
                    else:
                        user_location = weather.get_user_location()  
                        weather_info = weather.get_weather(user_location, OPENWEATHERMAP_API_KEY)  # Using the function from weather.py

                elif "the time" in query:
                    import timings 
                    place = re.search(r"(in|of|for) ([\w\s]+)", query, re.IGNORECASE)
                    # capture a sequence of word characters (\w) and spaces (\s) one or more times (+)

                    if place:
                        place = place[2]
                        tz = timings.get_timezone(place)
                        timing = timings.get_time(tz)
                        say(f"The Time in {place} is {timing}!")  

                    else:
                        local_time = datetime.datetime.now().strftime("%I:%M %p")
                        say(f"The Local Time is {local_time}!")      
