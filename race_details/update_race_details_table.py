from database_engine.engine import get_database_engine
from .race_details_from_api import get_race_details_from_api
from .parse_race_details import parse_race_details_data

# updates the race details in the sql table RACE_DETAILS


def update_the_race_details_table(round_num):
    engine = get_database_engine()

    race_details_data = get_race_details_from_api(round_num)
    df = parse_race_details_data(race_details_data)
    with engine.connect() as connection:
        df.to_sql('RACE_DETAILS', con=connection,
                  if_exists='append', index=False)
