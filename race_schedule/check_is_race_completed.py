import sqlalchemy as db
import datetime
from database_engine.engine import get_database_engine

# checks if race has been completed


def is_race_completed(round_num):
    engine = get_database_engine()
    with engine.connect() as connection:
        sql_query = "SELECT ComparisonDate FROM RACE_SCHEDULE WHERE Round = :round"
        result = connection.execute(
            db.text(sql_query), {"round": round_num}).fetchone()
    race_date = result[0]
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    return current_date > race_date
