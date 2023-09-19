from database_engine.engine import get_database_engine
import pandas as pd

# gets the upcoming race details from race schedule table to show when
# that race is coming given the round number


def get_race_from_database(round_num):
    engine = get_database_engine()
    
    with engine.connect() as connection:
        query = f"SELECT * FROM RACE_SCHEDULE WHERE Round = '{round_num}'"
        race_data = pd.read_sql(query, connection)

    race_data_info = {
                "RaceName": race_data["RaceName"][0],
                "Datetime": race_data["DisplayDate"][0] + " " + race_data["Time"][0],
            }
    
    return race_data_info
