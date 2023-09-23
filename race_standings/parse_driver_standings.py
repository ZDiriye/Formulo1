import pandas as pd
import datetime
import unittest

# takes the relevant data from the dictionary and returns it in a data frame


def parse_driver_standings_data(standings_data):
    standings_list = []
    current_date = datetime.date.today().strftime('%Y-%m-%d')

    for driver_data in standings_data:
        position = driver_data['position']
        driver_name = driver_data['Driver']['givenName'] + \
            ' ' + driver_data['Driver']['familyName']
        nationality = driver_data['Driver']['nationality']
        constructor = driver_data['Constructors'][0]['name']
        points = driver_data['points']
        wins = driver_data['wins']
        driverid = driver_data['Driver']['driverId']
        standings_list.append(
            (position,
             driver_name,
             nationality,
             constructor,
             points,
             wins,
             current_date,
             driverid))

    df = pd.DataFrame(
        standings_list,
        columns=[
            'Position',
            'Driver',
            'Nationality',
            'Car',
            'Points',
            'Wins',
            'Date',
            'DriverID'])

    return df


class TestParseDriverStandings(unittest.TestCase):
    def test_parse_driver_standings(self):
        mock_driver_standings = [
            {
                'Constructors': [
                    {
                        'name': 'Red Bull'
                    }
                ],
                'Driver': {
                    'givenName': 'Max',
                    'familyName': 'Verstappen',
                    'nationality': 'Dutch',
                    'driverId': 'max_verstappen'
                },
                'points': '314',
                'position': '1',
                'wins': '10'
            }
        ]

        result = parse_driver_standings_data(mock_driver_standings)

        current_date = datetime.date.today().strftime('%Y-%m-%d')
        expected_data = [
            ('1', 'Max Verstappen', 'Dutch', 'Red Bull',
             '314', current_date, 'max_verstappen')
        ]

        expected_df = pd.DataFrame(
            expected_data,
            columns=[
                'Position',
                'Driver',
                'Nationality',
                'Car',
                'Points',
                'Date',
                'DriverID'])

        # assert the function's return value matches the expected data
        pd.testing.assert_frame_equal(result, expected_df)
