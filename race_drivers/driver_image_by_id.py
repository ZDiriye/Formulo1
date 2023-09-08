from database_engine.engine import get_database_engine
import pandas as pd

# gets the driver image from the database given the ID


def get_driver_image_by_id(driver_id):
    engine = get_database_engine()
    
    with engine.connect() as connection:
        query = f"SELECT * FROM DRIVER_IMAGES WHERE DriverID = '{driver_id}'"
        driver_image = pd.read_sql(query, connection)
    return driver_image
