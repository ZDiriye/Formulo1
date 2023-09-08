import pandas as pd
import unittest
import datetime

# takes the relevant data from the dictionary and returns it in a data frame


def parse_constructor_standings_data(standings_data):
    standings_list = []
    current_date = datetime.date.today().strftime('%Y-%m-%d')
    for data in standings_data:
        position = data['position']
        name = data['Constructor']['name']
        points = data['points']
        constructor_id = data['Constructor']['constructorId']

        standings_list.append((position, name, points, current_date, constructor_id))
        df = pd.DataFrame(standings_list, columns=[
                          'Position', 'Name', 'Points', 'Date', 'ConstructorID'])

    return df


class TestParseConstructorStandings(unittest.TestCase):
    def test_parse_constructor_standings(self):
        mock_constructor_standings = [
            {
                'Constructor': {
                    'name': 'Red Bull',
                    'constructorId': 'red_bull'
                },
                'points': '503',
                'position': '1',
                'wins': '12'
                
            },
            {
                'Constructor': {
                    'name': 'Mercedes',
                    'constructorId': 'mercedes'
                },
                'points': '247',
                'position': '2',
                'wins': '0'
            }
        ]

        result = parse_constructor_standings_data(mock_constructor_standings)
        current_date = datetime.date.today().strftime('%Y-%m-%d')
        expected_data = [
            ('1', 'Red Bull', '503', current_date, 'red_bull'),
            ('2', 'Mercedes', '247', current_date, 'mercedes')
        ]

        expected_df = pd.DataFrame(expected_data, columns=[
                                   'Position', 'Name', 'Points', 'Date', 'ConstructorID'])

        # assert the function's return value matches the expected data
        pd.testing.assert_frame_equal(result, expected_df)
