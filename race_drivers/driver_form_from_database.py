from database_engine.engine import get_database_engine
import pandas as pd

# gets driver form from the database


def get_driver_form_from_database(driver_id):
    engine = get_database_engine()
    
    with engine.connect() as connection:
        sql_query = f"SELECT * FROM DRIVER_FORM WHERE DriverID  = '{driver_id}' AND Date = (SELECT MAX(Date) FROM DRIVER_FORM WHERE DriverID  = '{driver_id}')"
        driver_form_data = pd.read_sql(sql_query, connection)

    return driver_form_data
