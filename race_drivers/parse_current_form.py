import pandas as pd
import datetime

# takes the relevant data from the dictionary and returns it in a data frame


def parse_current_form_data(race_data_list, driver_id):
    standings_list = []

    current_year = datetime.datetime.now().year
    current_date = datetime.date.today().strftime('%Y-%m-%d')

    for race_data in race_data_list:
        race_name = race_data['raceName']
        year = current_year
        round_num = race_data['round']

        driver_data = race_data['Results'][0]
        position = driver_data['position']
        driver_name = driver_data['Driver']['givenName'] + \
            ' ' + driver_data['Driver']['familyName']
        car = driver_data['Constructor']['name']
        points = driver_data['points']
        status = driver_data['status']
        if position == '1':
            wins = 1
        else:
            wins = 0

        standings_list.append(
            (race_name,
             year,
             round_num,
             driver_name,
             car,
             position,
             points,
             status,
             wins,
             current_date,
             driver_id))

    df = pd.DataFrame(
        standings_list,
        columns=[
            'RaceName',
            'Year',
            'Round',
            'DriverName',
            'Team',
            'Position',
            'Points',
            'Status',
            'Wins',
            'Date',
            'DriverID'])

    return df
