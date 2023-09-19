from database_engine.engine import get_database_engine
from .driver_lineup_from_api import get_driver_lineup_from_api
from .parse_driver_lineup import parse_driver_lineup

# updates the driver lineup in the sql table DRIVER_LINEUP


def update_the_lineup_of_drivers(constructor_id):
    engine = get_database_engine()

    driver_lineup_data = get_driver_lineup_from_api(constructor_id)
    df = parse_driver_lineup(driver_lineup_data, constructor_id)
    with engine.connect() as connection:
        df.to_sql('DRIVER_LINEUP', con=connection,
                  if_exists='append', index=False)
