from database_engine.engine import get_database_engine
import pandas as pd

# gets constructor standings from the database


def get_constructor_standings_from_database():
    engine = get_database_engine()
    
    with engine.connect() as connection:
        sql_query = "SELECT * FROM CONSTRUCTORSTANDINGS"
        standings_data = pd.read_sql(sql_query, connection)
    return standings_data
