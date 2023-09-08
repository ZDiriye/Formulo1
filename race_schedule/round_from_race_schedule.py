from database_engine.engine import get_database_engine
import sqlalchemy as db

# to get the round from the race schedule table given the race name


def get_round_from_race_schedule(race_name):
    engine = get_database_engine()
    with engine.connect() as connection:
        sql_query = "SELECT Round FROM RACE_SCHEDULE WHERE RaceName =:race_name"
        round_num = connection.execute(
            db.text(sql_query), {"race_name": race_name}).fetchone()
    return round_num[0]

