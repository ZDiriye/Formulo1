import datetime
from race_schedule.update_race_schedule_table import update_the_race_schedule
from race_standings.update_constructor_standings_table import update_the_standings_of_constructors
from race_standings.update_driver_standings_table import update_the_standings_of_drivers

def check_update_schedule_standings_for_new_season():
    season_update_made = False

    current_date = datetime.date.today()

    if current_date.month == 3 and current_date.day == 1:
        if not season_update_made:
            update_the_race_schedule()
            update_the_standings_of_constructors()
            update_the_standings_of_drivers()

            season_update_made = True
    elif current_date.month == 3 and current_date.day == 2:
        season_update_made = False
