from database_engine.engine import get_database_engine
import pandas as pd

# gets driver standings from the database


def get_driver_standings_from_database():
    engine = get_database_engine()
    
    with engine.connect() as connection:
        sql_query = "SELECT * FROM DRIVERSTANDINGS"
        standings_data = pd.read_sql(sql_query, connection)
    return standings_data
