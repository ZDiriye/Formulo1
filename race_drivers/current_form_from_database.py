from database_engine.engine import get_database_engine
import pandas as pd

# gets current form from the database


def get_current_form_from_database(driver_id):
    engine = get_database_engine()
    
    with engine.connect() as connection:
        sql_query = f"SELECT * FROM CURRENT_FORM WHERE DriverID  = '{driver_id}' AND Date = (SELECT MAX(Date) FROM CURRENT_FORM WHERE DriverID  = '{driver_id}')"
        current_form_data = pd.read_sql(sql_query, connection)

    return current_form_data
