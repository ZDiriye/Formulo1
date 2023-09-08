from database_engine.engine import get_database_engine
import pandas as pd

# gets team images from the database


def get_team_images_from_database():
    engine = get_database_engine()
    
    with engine.connect() as connection:
        query = 'SELECT * FROM TEAM_IMAGES'
        team_images = pd.read_sql(query, connection)
    return team_images
