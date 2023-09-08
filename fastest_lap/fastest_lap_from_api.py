import requests
import unittest
from unittest.mock import Mock, patch

# get the fastest lap from api given the round


def get_fastest_lap_from_api(round_number):
    url = f"http://ergast.com/api/f1/current/{round_number}/fastest/1/results.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        race_data = data['MRData']['RaceTable']['Races'][0]
        return race_data
    except requests.exceptions.RequestException:
        return None  # return None when an API error occurs


class TestFastestLapFromApi(unittest.TestCase):
    @patch('fastest_lap.fastest_lap_from_api.requests.get')
    def test_fastest_lap_from_api(self, mock_get):
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
        result = get_fastest_lap_from_api(round_number)

        expected_result = {
            "season": "2023",
            "round": "4",
        }

        # assert that the function's return value matches the mocked query
        # result
        self.assertEqual(result, expected_result)
