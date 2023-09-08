from database_engine.engine import get_database_engine
import pandas as pd

# gets country images from the database


def get_country_images_from_database():
    engine = get_database_engine()
    
    with engine.connect() as connection:
        query = 'SELECT * FROM COUNTRY_IMAGES'
        country_images = pd.read_sql(query, connection)
    return country_images
