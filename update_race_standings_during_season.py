from race_standings.date_in_driver_standings import get_date_in_driver_standings
from race_schedule.last_completed_race_date import get_last_completed_race_date
from race_standings.update_constructor_standings_table import update_the_standings_of_constructors
from race_standings.update_driver_standings_table import update_the_standings_of_drivers

# checks if the CONSTRUCTORSTANDINGS, DRIVERSTANDINGS and RACE_SCHEDULE
# needs updating table if so calls the relevant apis


def check_update_standings_during_season():
    last_completed_race = get_last_completed_race_date()
    max_date_in_standings = get_date_in_driver_standings()

    if max_date_in_standings is None or max_date_in_standings < last_completed_race:
        update_the_standings_of_drivers()
        update_the_standings_of_constructors()
    elif max_date_in_standings is not None and max_date_in_standings > last_completed_race:
        return
    else:
        return

