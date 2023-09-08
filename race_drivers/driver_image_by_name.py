from database_engine.engine import get_database_engine
import pandas as pd

# gets the driver image from the database given the name


def get_driver_image_by_name(driver_name):
    engine = get_database_engine()
    
    with engine.connect() as connection:
        query = f"SELECT * FROM DRIVER_IMAGES WHERE DriverName = '{driver_name}'"
        driver_image = pd.read_sql(query, connection)
    return driver_image
