from database_engine.engine import get_database_engine
from race_details.update_race_details_table import update_the_race_details_table
from fastest_lap.update_fastest_lap_table import update_the_fastest_lap_table
import sqlalchemy as db
import datetime

# checks if the RACE_DETAILS and FASTEST_LAP table needs updating
# if so calls the relevant apis

def check_update_race_details_during_season(race_name, round_num):
    engine = get_database_engine()
    with engine.connect() as connection:
        sql_query = "SELECT Year FROM RACE_DETAILS WHERE RaceName = :race_name"
        existing_race_year = connection.execute(
            db.text(sql_query), {"race_name": race_name}).fetchone()

    current_year = datetime.datetime.now().year

    if existing_race_year is None or existing_race_year[0] != current_year: 
        update_the_race_details_table(round_num)
        update_the_fastest_lap_table(round_num)
    else:
        return
