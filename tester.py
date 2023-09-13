import requests
import pprint
# gets the race details from api  given a round


def get_race_details_from_api(constructor_id):
    url = f"http://ergast.com/api/f1/current/last/constructors/{constructor_id}/results.json"
    url = f"http://ergast.com/api/f1/current/constructors/{constructor_id}/results.json"

    try:
        response = requests.get(url)
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        return None  # return None when an API error occurs


if __name__ == "__main__":
    pprint.pprint(get_race_details_from_api("alphatauri"))