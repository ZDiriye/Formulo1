import sqlalchemy as db
import datetime
from database_engine.engine import get_database_engine

# checks if last completed race is completed


def get_last_completed_race_date():
    engine = get_database_engine()
    with engine.connect() as connection:
        sql_query = "SELECT MAX(ComparisonDate) FROM RACE_SCHEDULE WHERE ComparisonDate < :current_date"
        result = connection.execute(
            db.text(sql_query), {
                "current_date": datetime.date.today()}).fetchone()
    if result[0] is not None:
        return datetime.datetime.strptime(result[0], '%Y-%m-%d').date()
    else:
        return None
