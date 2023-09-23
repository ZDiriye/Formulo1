from database_engine.engine import get_database_engine
import pandas as pd

# gets race details from the database given the race name


def get_race_details_from_database(race_name):
    engine = get_database_engine()
    
    with engine.connect() as connection:
        query = f"SELECT * FROM RACE_DETAILS WHERE RaceName = '{race_name}' AND Year = (SELECT MAX(Year) FROM RACE_DETAILS WHERE RaceName  = '{race_name}')"
        race_details_data = pd.read_sql(query, connection)
    
    return race_details_data
