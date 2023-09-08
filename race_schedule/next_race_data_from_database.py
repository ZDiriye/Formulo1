from database_engine.engine import get_database_engine
import pandas as pd
import datetime

# for the race countdown on the home page


def get_next_race_data_from_database():
    engine = get_database_engine()
    
    with engine.connect() as connection:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        query = f"SELECT * FROM RACE_SCHEDULE WHERE ComparisonDate >= '{current_date}' ORDER BY comparisonDate LIMIT 1"
        next_race_data = pd.read_sql(query, connection)

    next_race_info = {
            "RaceName": next_race_data["RaceName"][0],
            "Datetime": next_race_data["Date"][0] +
            " " +
            next_race_data["Time"][0],
        }
    return next_race_info
