from database_engine.engine import get_database_engine
import pandas as pd

# gets race schedule from the database


def get_circuit_images_from_database():
    engine = get_database_engine()
    
    with engine.connect() as connection:
        query = 'SELECT * FROM RACE_IMAGES'
        race_images = pd.read_sql(query, connection)
    return race_images
