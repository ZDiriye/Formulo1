import pandas as pd
import unittest
from unittest.mock import patch
import datetime

# takes the relevant data from the dictionary and returns it in a data frame


def parse_fastest_lap_data(race_data):
    fastest_lap_list = []

    current_year = datetime.datetime.now().year

    race_name = race_data['raceName']

    for driver_data in race_data['Results']:
        driver_name = driver_data['Driver']['givenName'] + \
            ' ' + driver_data['Driver']['familyName']
        fastest_lap = driver_data['FastestLap']['Time']['time']
        fastest_lap_list.append(
            (race_name, driver_name, fastest_lap, current_year))

    df = pd.DataFrame(fastest_lap_list, columns=[
                      'RaceName', 'Driver', 'FastestLap', 'CurrentYear'])

    return df


class TestParseFastestLap(unittest.TestCase):
    @patch('datetime.datetime')
    def test_parse_fastest_lap(self, mock_datetime):
        mock_now = mock_datetime.now.return_value
        mock_now.year = 2023

        mock_race_data = {
            "raceName": "Bahrain Grand Prix",
            "Results": [
                {
                    "Driver": {"givenName": "Lewis", "familyName": "Hamilton"},
                    "FastestLap": {"Time": {"time": "1:33.123"}},
                },
                {
                    "Driver": {"givenName": "Max", "familyName": "Verstappen"},
                    "FastestLap": {"Time": {"time": "1:33.456"}},
                },
            ],
        }

        result = parse_fastest_lap_data(mock_race_data)

        expected_data = [
            ("Bahrain Grand Prix", "Lewis Hamilton", "1:33.123", 2023),
            ("Bahrain Grand Prix", "Max Verstappen", "1:33.456", 2023),
        ]
        expected_df = pd.DataFrame(
            expected_data,
            columns=[
                'RaceName',
                'Driver',
                'FastestLap',
                'CurrentYear'])

        # assert the function's return value matches the expected data
        pd.testing.assert_frame_equal(result, expected_df)
