import sqlalchemy as db
import datetime
from database_engine.engine import get_database_engine

# gets the max date in the sql table DRIVER_FORM given driver id


def get_date_in_driver_form_table(driver_id):
    engine = get_database_engine()
    with engine.connect() as connection:
        sql_query = "SELECT MAX(Date) FROM DRIVER_FORM WHERE DriverID = :driver_id;"

        result = connection.execute(
            db.text(sql_query), {"driver_id": driver_id}).fetchone()

    if result[0] is not None:  # table is not empty
        return datetime.datetime.strptime(result[0], '%Y-%m-%d').date()
    else:
        return None
