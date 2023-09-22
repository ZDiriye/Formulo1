from database_engine.engine import get_database_engine
import pandas as pd

def get_teams_championship_position(constructor_id):
    engine = get_database_engine()
    
    with engine.connect() as connection:
        query = f"SELECT Position FROM CONSTRUCTORSTANDINGS WHERE ConstructorID = '{constructor_id}'"
        position_data = pd.read_sql(query, connection)

    championship_position_data = {
            "Position": position_data["Position"][0]
        }
    return championship_position_data
