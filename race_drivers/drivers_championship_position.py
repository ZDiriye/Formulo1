from database_engine.engine import get_database_engine
import pandas as pd

def get_drivers_championship_position(driver_id):
    engine = get_database_engine()
    
    with engine.connect() as connection:
        query = f"SELECT Position FROM DRIVERSTANDINGS WHERE DriverID = '{driver_id}'"
        position_data = pd.read_sql(query, connection)

    championship_position_data = {
            "Position": position_data["Position"][0]
        }
    return championship_position_data
