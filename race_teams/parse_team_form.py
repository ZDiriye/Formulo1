import pandas as pd
import datetime

# takes the relevant data from the dictionary and returns it in a data frame


def parse_team_form_data(team_form_data, constructor_id):
    standings_list = []

    current_date = datetime.date.today().strftime('%Y-%m-%d')

    for team_data in team_form_data:
        round_num = team_data['round']
        race_name = team_data['raceName']

        total_points = 0

        race_results = team_data['Results']

        for driver_data in race_results:
            points = int(driver_data['points'])
            total_points += points

        standings_list.append(
            (round_num,
             race_name,
             total_points,
             current_date,
             constructor_id))

    df = pd.DataFrame(
        standings_list,
        columns=[
            'Round',
            'RaceName',
            'Points',
            'Date',
            'ConstructorID'])

    return df
