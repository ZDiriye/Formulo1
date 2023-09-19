import requests

# gets the race details from api  given a round


def get_team_form_from_api(constructor_id):
    url = f"http://ergast.com/api/f1/current/constructors/{constructor_id}/results.json"
    try:
        response = requests.get(url)
        data = response.json()
        team_form_data = data['MRData']['RaceTable']['Races']
        return team_form_data
    except requests.exceptions.RequestException:
        return None  # return None when an API error occurs
