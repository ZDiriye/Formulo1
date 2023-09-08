from database_engine.engine import get_database_engine
from .current_form_from_api import get_current_form_from_api
from .parse_current_form import parse_current_form_data

# updates the race details in the sql table CURRENT_FORM


def update_the_current_form_of_drivers(driver_id):
    engine = get_database_engine()

    current_form_data = get_current_form_from_api(driver_id)
    df = parse_current_form_data(current_form_data, driver_id)
    with engine.connect() as connection:
        df.to_sql('CURRENT_FORM', con=connection,
                  if_exists='append', index=False)
