import pandas as pd
import datetime
import unittest
from unittest.mock import patch

# takes the relevant data from the dictionary and returns it in a data frame


def parse_race_details_data(race_data):
    standings_list = []

    year = datetime.datetime.now().year

    race_name = race_data['raceName']

    for driver_data in race_data['Results']:
        position = driver_data['position']
        number = driver_data['number']
        driver_name = driver_data['Driver']['givenName'] + \
            ' ' + driver_data['Driver']['familyName']
        car = driver_data['Constructor']['name']
        laps = driver_data['laps']

        if 'Time' in driver_data:
            time = driver_data['Time']['time']
        elif driver_data['status'] == "+1 Lap" or driver_data['status'] == "+2 Laps":
            time = driver_data['status']  # shows the status in the time column
        else:
            time = "DNF"
            position = "NC"  # driver did not finish if the if and elif statement was not true
        points = driver_data['points']
        standings_list.append(
            (race_name,
             position,
             number,
             driver_name,
             car,
             laps,
             time,
             points,
             year))

    df = pd.DataFrame(
        standings_list,
        columns=[
            'RaceName',
            'Position',
            'Number',
            'DriverName',
            'Car',
            'Laps',
            'Time',
            'Points',
            'Year'])

    return df


class TestParseRaceDetails(unittest.TestCase):
    @patch('datetime.datetime')
    def test_parse_race_details(self, mock_datetime):
        mock_now = mock_datetime.now.return_value
        mock_now.year = 2023

        mock_race_data = {
            "raceName": "Canadian Grand Prix",
            "Results": [
                {
                    "Constructor": {"name": "Red Bull"},
                    "Driver": {"givenName": "Max", "familyName": "Verstappen"},
                    "FastestLap": {"Time": {"time": "1:36.236"}},
                    "Time": {"time": "1:33:56.736"},
                    "position": "1",
                    "number": "1",
                    "laps": "57",
                    "points": "25",
                    "status": "Finished"
                }
            ]
        }

        result = parse_race_details_data(mock_race_data)

        expected_data = [
            ("Canadian Grand Prix", "1", "1", "Max Verstappen",
             "Red Bull", "57", "1:33:56.736", "25", 2023)
        ]
        expected_df = pd.DataFrame(
            expected_data,
            columns=[
                'RaceName',
                'Position',
                'Number',
                'DriverName',
                'Car',
                'Laps',
                'Time',
                'Points',
                'Year'])

        # assert the function's return value matches the expected data
        pd.testing.assert_frame_equal(result, expected_df)
