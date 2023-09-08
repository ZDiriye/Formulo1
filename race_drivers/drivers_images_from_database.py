from database_engine.engine import get_database_engine
import pandas as pd

# gets all driver images from the database


def get_drivers_images_from_database():
    engine = get_database_engine()
    
    with engine.connect() as connection:
        query = 'SELECT * FROM DRIVER_IMAGES'
        driver_images = pd.read_sql(query, connection)
    return driver_images
