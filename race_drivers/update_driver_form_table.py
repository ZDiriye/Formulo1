from database_engine.engine import get_database_engine
from .driver_form_from_api import get_driver_form_from_api
from .parse_driver_form import parse_driver_form_data

# updates the drivers form in the sql table DRIVER_FORM


def update_the_form_of_drivers(driver_id):
    engine = get_database_engine()

    driver_form_data = get_driver_form_from_api(driver_id)
    df = parse_driver_form_data(driver_form_data, driver_id)
    with engine.connect() as connection:
        df.to_sql('DRIVER_FORM', con=connection,
                  if_exists='append', index=False)
