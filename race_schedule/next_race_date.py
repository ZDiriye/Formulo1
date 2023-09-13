from database_engine.engine import get_database_engine
import sqlalchemy as db
import datetime

# for the race countdown on the home page


def get_next_race_date():
    engine = get_database_engine()
    with engine.connect() as connection:
        sql_query = "SELECT MIN(Date) FROM RACE_SCHEDULE WHERE Date >= :current_date"
        result = connection.execute(
            db.text(sql_query), {
                "current_date": datetime.date.today()}).fetchone()
    if result[0] is not None:
        return datetime.datetime.strptime(result[0], '%Y-%m-%d').date()
    else:
        return None
