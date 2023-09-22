import pandas as pd
import datetime

# takes the relevant data from the dictionary and returns it in a data frame


def parse_driver_lineup(driver_lineup_data, constructor_id):
    standings_list = []
    current_date = datetime.date.today().strftime('%Y-%m-%d')

    for driver_data in driver_lineup_data:

        driver_name = driver_data['Driver']['givenName'] + \
            ' ' + driver_data['Driver']['familyName']

        standings_list.append(
            (constructor_id,
             driver_name,
             current_date
             ))

    df = pd.DataFrame(
        standings_list,
        columns=[
            'ConstructorID',
            'DriverName',
            'Date'
            ])

    return df
