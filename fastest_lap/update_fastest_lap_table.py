from database_engine.engine import get_database_engine
from .fastest_lap_from_api import get_fastest_lap_from_api
from .parse_fastest_lap import parse_fastest_lap_data

# updates the fastest lap in the sql table FASTEST_LAP


def update_the_fastest_lap_table(round_num):
    Engine = get_database_engine()

    fastest_lap_data = get_fastest_lap_from_api(round_num)
    df = parse_fastest_lap_data(fastest_lap_data)
    with Engine.connect() as connection:
        df.to_sql('FASTEST_LAP', con=connection,
                  if_exists='append', index=False)
