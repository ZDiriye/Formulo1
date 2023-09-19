from database_engine.engine import get_database_engine
import pandas as pd

# gets winner of the given race from the database

def get_winner_name_from_database(race_name):
    engine = get_database_engine()
    
    with engine.connect() as connection:
        sql_query = f"SELECT DriverName FROM RACE_DETAILS WHERE Year = (SELECT MAX(Year) FROM RACE_DETAILS WHERE RaceName = '{race_name}') AND RaceName = '{race_name}' LIMIT 1"
        winner_data = pd.read_sql(sql_query, connection)

    winner_name = {
            "DriverName": winner_data["DriverName"][0]
            }

    return winner_name