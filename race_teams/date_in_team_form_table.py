import sqlalchemy as db
import datetime
from database_engine.engine import get_database_engine

# gets the max date in the sql table TEAM_FORM given constructor id


def get_date_in_team_form_table(constructor_id):
    engine = get_database_engine()
    with engine.connect() as connection:
        sql_query = "SELECT MAX(Date) FROM TEAM_FORM WHERE ConstructorID = :constructor_id;"

        result = connection.execute(
            db.text(sql_query), {"constructor_id": constructor_id}).fetchone()

    if result[0] is not None:  # table is not empty
        return datetime.datetime.strptime(result[0], '%Y-%m-%d').date()
    else:
        return None
