import requests
import unittest
from unittest.mock import Mock, patch
# gets the race schedule data from the api and returns it in dictionary form


def get_race_schedule_from_api():
    url = "http://ergast.com/api/f1/current.json"
    try:
        response = requests.get(url)
        data = response.json()
        race_schedule = data['MRData']['RaceTable']['Races']
        return race_schedule
    except requests.exceptions.RequestException:
        return None  # return None when an API error occurs

class TestRaceScheduleFromApi(unittest.TestCase):
    @patch('race_schedule.race_schedule_from_api.requests.get')
    def test_race_schedule_from_api(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {
            "MRData": {
                "RaceTable": {
                    "Races":
                        {
                            "season": "2023",
                            "round": "4",
                        }
                }
            }
        }
        mock_get.return_value = mock_response

        result = get_race_schedule_from_api()

        expected_result = {
            "season": "2023",
            "round": "4",
        }

        # assert the function's return value matches the expected data
        self.assertEqual(result, expected_result)
