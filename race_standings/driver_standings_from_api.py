import requests
import unittest
from unittest.mock import Mock, patch

# gets the current driver standings data from the api and returns it in
# dictionary form


def get_driver_standings_from_api():
    url = "http://ergast.com/api/f1/current/driverStandings.json"
    try:
        response = requests.get(url)
        standings = response.json()
        standings_data = standings['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
        return standings_data
    except requests.exceptions.RequestException:
        return None  # return None when an API error occurs

class TestDriverStandingsFromApi(unittest.TestCase):
    @patch('race_standings.driver_standings_from_api.requests.get')
    def test_driver_standings_from_api(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {
            "MRData": {
                "StandingsTable": {
                    "StandingsLists": [{
                        "DriverStandings":
                        [{"position": "1",
                            "points": "25", }]
                    }
                    ]
                }
            }
        }
        mock_get.return_value = mock_response

        result = get_driver_standings_from_api()

        expected_result = [{
            "position": "1",
            "points": "25",
        }]

        # assert the function's return value matches the expected data
        self.assertEqual(result, expected_result)
