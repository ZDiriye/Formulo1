import datetime
from race_drivers.update_driver_form_table import update_the_form_of_drivers

def check_update_driver_form_new_season(driver_id):
    season_update_made = False

    current_date = datetime.date.today()

    if current_date.month == 3 and current_date.day == 1:
        if not season_update_made:
            update_the_form_of_drivers(driver_id)

            season_update_made = True
    elif current_date.month == 3 and current_date.day == 2:
        season_update_made = False
