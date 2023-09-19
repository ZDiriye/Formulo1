import requests
import pprint
# gets the race schedule data from the api and returns it in dictionary form


def get_race_schedule_from_api():
    url = "http://ergast.com/api/f1/current.json"
    try:
        response = requests.get(url)
        data = response.json()
        race_schedule = data
        return race_schedule
    except requests.exceptions.RequestException:
        return None  # return None when an API error occurs


pprint.pprint(get_race_schedule_from_api())