from database_engine.engine import get_database_engine
import pandas as pd

# gets driver lineup from the database given the constructor id

def get_driver_lineup_from_database(constructor_id):
    engine = get_database_engine()
    
    with engine.connect() as connection:
        sql_query = f"SELECT * FROM DRIVER_LINEUP WHERE ConstructorID  = '{constructor_id}' AND Date = (SELECT MAX(Date) FROM DRIVER_LINEUP WHERE ConstructorID  = '{constructor_id}')"
        driver_lineup = pd.read_sql(sql_query, connection)

    driver_lineup_info = {
            "DriverName1": driver_lineup["DriverName"][0],
            "DriverName2": driver_lineup["DriverName"][1],
        }
    
    return driver_lineup_info
