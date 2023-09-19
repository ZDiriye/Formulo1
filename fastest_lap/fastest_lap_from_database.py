from database_engine.engine import get_database_engine
import pandas as pd

# gets fastest lap from database

def get_fastest_lap_from_database(race_name):
    engine = get_database_engine()
    
    with engine.connect() as connection:
        query = f"SELECT * FROM FASTEST_LAP WHERE RaceName = '{race_name}' AND Year = (SELECT MAX(Year) FROM FASTEST_LAP WHERE RaceName = '{race_name}')"
        fastest_lap_data = pd.read_sql(query, connection)
    
    fastest_lap_data_info = {
                "Driver": fastest_lap_data["Driver"][0],
                "FastestLap": fastest_lap_data["FastestLap"][0],
            }
    return fastest_lap_data_info
