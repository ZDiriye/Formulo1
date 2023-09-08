from database_engine.engine import get_database_engine
from .driver_standings_from_api import get_driver_standings_from_api
from .parse_driver_standings import parse_driver_standings_data

# updates the driver standings in the sql table DRIVERSTANDINGS


def update_the_standings_of_drivers():
    engine = get_database_engine()

    current_standings_data = get_driver_standings_from_api()
    df = parse_driver_standings_data(current_standings_data)
    with engine.connect() as connection:
        df.to_sql('DRIVERSTANDINGS', con=connection,
                  if_exists='append', index=False)
