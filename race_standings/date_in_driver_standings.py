import sqlalchemy as db
import datetime
from database_engine.engine import get_database_engine

# gets the date in the sql table DRIVERSTANDINGS


def get_date_in_driver_standings():
    engine = get_database_engine()
    with engine.connect() as connection:
        sql_query = "SELECT MAX(Date) FROM DRIVERSTANDINGS"
        result = connection.execute(db.text(sql_query)).fetchone()

    if result[0] is not None:  # table is not empty
        return datetime.datetime.strptime(result[0], '%Y-%m-%d').date()
    else:
        return None


