from .race_schedule_from_api import get_race_schedule_from_api
from .parse_race_schedule import parse_race_schedule_data
from database_engine.engine import get_database_engine

# updates the new race schedule in the sql table RACE_SCHEDULE


def update_the_race_schedule():
    engine = get_database_engine()

    race_schedule_data = get_race_schedule_from_api()
    df = parse_race_schedule_data(race_schedule_data)
    with engine.connect() as connection:
        df.to_sql('RACE_SCHEDULE', con=connection,
                  if_exists='replace', index=False)
