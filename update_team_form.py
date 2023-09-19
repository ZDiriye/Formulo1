from race_teams.update_driver_lineup import update_the_lineup_of_drivers
from race_teams.update_team_form_table import update_the_form_of_teams

# checks if the RACE_SCHEDULE and TEAM_FORM table needs updating, 
# if so calls the relevant apis

def check_update_team_form(constructor_id):
    update_the_form_of_teams(constructor_id)
    update_the_lineup_of_drivers(constructor_id)
