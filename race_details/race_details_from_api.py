import requests
import unittest
from unittest.mock import Mock, patch
# gets the race details from api  given a round


def get_race_details_from_api(round_num):
    url = f"http://ergast.com/api/f1/current/{round_num}/results.json"
    try:
        response = requests.get(url)
        data = response.json()
        race_data = data['MRData']['RaceTable']['Races'][0]
        return race_data
    except requests.exceptions.RequestException:
        return None  # return None when an API error occurs


class TestRaceDetailsFromApi(unittest.TestCase):
    @patch('race_details.race_details_from_api.requests.get')
    def test_race_details_from_api(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {
            "MRData": {
                "RaceTable": {
                    "Races": [
                        {
                            "season": "2023",
                            "round": "4",
                        }
                    ]
                }
            }
        }
        mock_get.return_value = mock_response

        round_number = 1
        result = get_race_details_from_api(round_number)

        expected_result = {
            "season": "2023",
            "round": "4",
        }
        # assert the function's return value matches the expected data
        self.assertEqual(result, expected_result)
