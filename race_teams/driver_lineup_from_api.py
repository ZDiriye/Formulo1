import requests
# gets the race details from api  given a round


def get_driver_lineup_from_api(constructor_id):
    url = f"http://ergast.com/api/f1/current/last/constructors/{constructor_id}/results.json"
    try:
        response = requests.get(url)
        data = response.json()
        driver_lineup_data = data['MRData']['RaceTable']['Races'][0]['Results']
        return driver_lineup_data
    except requests.exceptions.RequestException:
        return None  # return None when an API error occurs
