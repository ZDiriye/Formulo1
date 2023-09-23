from database_engine.engine import get_database_engine
import pandas as pd

# gets championship data in the sql table DRIVERSTANDINGS given driver id


def get_drivers_championship_data(driver_id):
    engine = get_database_engine()
    
    with engine.connect() as connection:
        query = f"SELECT Wins, Position FROM DRIVERSTANDINGS WHERE DriverID = '{driver_id}'"
        position_data = pd.read_sql(query, connection)

    championship_position_data = {
            "Position": position_data["Position"][0],
            "Wins": position_data["Wins"][0]
        }
    return championship_position_data

