from database_engine.engine import get_database_engine
import pandas as pd

# gets the official team image from the database given the constructor id


def get_official_team_image_by_id(constructor_id):
    engine = get_database_engine()
    
    with engine.connect() as connection:
        query = f"SELECT * FROM OFFICIAL_TEAM_IMAGES WHERE ConstructorID = '{constructor_id}'"
        team_image = pd.read_sql(query, connection)

    teams_image_info = {
            "ImagePath": team_image["ImagePath"][0],
            "TeamName": team_image["TeamName"][0],
        }
    return teams_image_info
