import pandas as pd
from dateutil.parser import parse
import unittest
from unittest.mock import patch
import pytz
# takes the relevant data from the dictionary and returns it in a data frame

def get_correct_time(time_str, date_str):
    # Define the target timezone (Europe/London)
    target_timezone = pytz.timezone('Europe/London')
    date_obj = parse(date_str)
    
    # check if the date is within the BST period (e.g., April to October)
    is_bst_period = date_obj.month >= 4 and date_obj.month <= 10
    
    if is_bst_period:
        # convert the Zulu time datetime object to BST
        time = parse(time_str)
        london_time = time.astimezone(target_timezone)
        formatted_time = london_time.strftime('%H:%M:%S')
    else:
        formatted_time = parse(time_str).strftime('%H:%M:%S')
    
    return formatted_time

def parse_race_schedule_data(race_schedules):
    race_schedule_list = []

    for race_schedule in race_schedules:
        round = race_schedule['round']
        season = race_schedule['season']
        race_name = race_schedule['raceName']
        date_str = race_schedule['date']
        time_str = race_schedule.get('time')
        comparisonDate = race_schedule['date']
        circuit_name = race_schedule['Circuit']['circuitName']
        nationality = race_schedule['Circuit']['Location']['country']

        # check if the zulu time needs to be converted to bst
        time = get_correct_time(time_str, date_str)

        # convert date from '2023-03-05' to 'March 5, 2023'
        date_obj = parse(date_str)
        formatted_date = date_obj.strftime('%b %d, %Y')

        race_schedule_list.append(
            (round,
             season,
             race_name,
             formatted_date,
             time,
             comparisonDate,
             circuit_name,
             nationality))

    df = pd.DataFrame(
        race_schedule_list,
        columns=[
            'Round',
            'Season',
            'RaceName',
            'Date',
            'Time',  
            'ComparisonDate',
            'CircuitName',
            'Nationality'])
    return df

class TestParseRaceSchedule(unittest.TestCase):
    @patch('dateutil.parser.parse')
    def test_parse_race_schedule(self, mock_parse):
        mock_parse.side_effect = lambda x: parse(x)

        mock_race_schedules = [
            {
                'Circuit': {
                    'circuitName': 'Bahrain International Circuit',
                    'Location': {
                        'country': 'Bahrain'  # Add the country data here
                    }
                },
                'date': '2023-03-05',
                'raceName': 'Bahrain Grand Prix',
                'round': '1',
                'season': '2023',
                'time': '15:00:00Z'
            }
        ]

        result = parse_race_schedule_data(mock_race_schedules)

        expected_data = [
            ("1", "2023", "Bahrain Grand Prix", "Mar 05, 2023",
            "15:00:00", "2023-03-05", "Bahrain International Circuit", "Bahrain")
        ]

        expected_df = pd.DataFrame(
            expected_data,
            columns=[
                'Round',
                'Season',
                'RaceName',
                'Date',
                'Time',
                'ComparisonDate',
                'CircuitName',
                'Nationality'])

        # cnvert the "Time" column in the actual DataFrame to string
        result['Time'] = result['Time'].astype(str)

        pd.testing.assert_frame_equal(result, expected_df)
