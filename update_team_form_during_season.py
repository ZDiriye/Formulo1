from race_teams.update_driver_lineup import update_the_lineup_of_drivers
from race_teams.update_team_form_table import update_the_form_of_teams
from race_schedule.last_completed_race_date import get_last_completed_race_date
from race_teams.date_in_team_form_table import get_date_in_team_form_table

# checks if the DRIVER_LINEUP and TEAM_FORM table needs updating


def check_update_team_form_during_season(constructor_id):
    last_completed_race = get_last_completed_race_date()
    date_in_team_form = get_date_in_team_form_table(constructor_id)

    if date_in_team_form is None or date_in_team_form < last_completed_race:
        update_the_form_of_teams(constructor_id)
        update_the_lineup_of_drivers(constructor_id)
    elif date_in_team_form is not None and date_in_team_form > last_completed_race:
        return
    else:
        return
