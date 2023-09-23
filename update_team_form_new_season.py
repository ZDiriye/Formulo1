import datetime
from race_teams.update_driver_lineup import update_the_lineup_of_drivers
from race_teams.update_team_form_table import update_the_form_of_teams

# update the DRIVER_LINEUP and TEAM_FORM table for new season


def check_update_team_form_new_season(constructor_id):
    season_update_made = False

    current_date = datetime.date.today()

    if current_date.month == 3 and current_date.day == 1:
        if not season_update_made:
            update_the_lineup_of_drivers(constructor_id)
            update_the_form_of_teams(constructor_id)

            season_update_made = True
    elif current_date.month == 3 and current_date.day == 2:
        season_update_made = False
