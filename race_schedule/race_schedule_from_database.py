from database_engine.engine import get_database_engine
import pandas as pd

# gets race schedule from the database


def get_race_schedule_from_database():
    engine = get_database_engine()
    
    with engine.connect() as connection:
        query = 'SELECT * FROM RACE_SCHEDULE'
        schedule_data = pd.read_sql(query, connection)
    return schedule_data
