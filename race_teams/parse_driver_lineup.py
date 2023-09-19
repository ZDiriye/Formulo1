import pandas as pd


# takes the relevant data from the dictionary and returns it in a data frame


def parse_driver_lineup(driver_lineup_data, constructor_id):
    standings_list = []

    for driver_data in driver_lineup_data:

        driver_name = driver_data['Driver']['givenName'] + \
            ' ' + driver_data['Driver']['familyName']

        standings_list.append(
            (constructor_id,
             driver_name,
             ))

    df = pd.DataFrame(
        standings_list,
        columns=[
            'ConstructorID',
            'DriverName',
            ])

    return df
