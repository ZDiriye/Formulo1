from database_engine.engine import get_database_engine
import pandas as pd

# gets team images from the database


def get_official_team_images_from_database():
    engine = get_database_engine()
    
    with engine.connect() as connection:
        query = 'SELECT * FROM OFFICIAL_TEAM_IMAGES'
        official_team_images = pd.read_sql(query, connection)
    return official_team_images
