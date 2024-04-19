from speak import say
import pywhatkit
import wikipedia
import webbrowser
import requests

# This function will open Google search results and also speak out some specified number of lines after searching on Wikipedia.

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("google search","")
        query = query.replace("google","")
        say("Here's what I found on Google!")

        try:
            pywhatkit.search(query) # Google search results
            result = googleScrap.summary(query, 1)  # Number of lines we want it to speak with the search results.
            say(result)

        except:
            say(" ")

# ------------------GOOGLE CUSTOM SEARCH API-------------------------------- 

# def searchGoogle(query, api_key, search_engine_id):
#     base_url = "https://www.googleapis.com/customsearch/v1"
#     params = {
#         "key": api_key,
#         "cx": search_engine_id,
#         "q": query
#     }

#     response = requests.get(base_url, params=params)
#     data = response.json()

#     search_results = data.get("items", [])
#     if search_results:
#         for idx, result in enumerate(search_results, start=1):
#             print(f"{idx}. {result['title']}: {result['link']}")
#             if idx == 1:
#                 result_text = f"Here's what I found: {result['snippet']}"
#                 say(result_text)  # Speak the summary of the first result
#     else:
#         print("No search results found.")  
             

# This function will open the first YouTube video for your search. 
def searchYoutube(query):
    if "youtube" in query:
        say("Here's what I found on Youtube!") 
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        yt  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(yt)
        pywhatkit.playonyt(query) # Plays the first video related to that query

# This function will open Wikipedia search results.
def searchWikipedia(query):
    if "wikipedia" in query:
        say("Searching on wikipedia..")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        say("Here's what I found!") 
        wiki = wikipedia.summary(query,sentences = 2) # Number of lines we want it to speak 
        say("According to wikipedia..")
        print(wiki) # Printing the wikipedia results
        say(wiki)