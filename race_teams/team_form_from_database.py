from database_engine.engine import get_database_engine
import pandas as pd

# gets team form from the database


def get_team_form_from_database(constructor_id):
    engine = get_database_engine()
    
    with engine.connect() as connection:
        sql_query = f"SELECT * FROM TEAM_FORM WHERE ConstructorID  = '{constructor_id}' AND Date = (SELECT MAX(Date) FROM TEAM_FORM WHERE ConstructorID  = '{constructor_id}')"
        team_form_data = pd.read_sql(sql_query, connection)

    return team_form_data
