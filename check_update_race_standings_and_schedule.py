from race_standings.date_in_driver_standings import get_date_in_driver_standings
from race_schedule.last_completed_race_date import get_last_completed_race_date
from race_schedule.next_race_date import get_next_race_date
from race_standings.update_constructor_standings_table import update_the_standings_of_constructors
from race_standings.update_driver_standings_table import update_the_standings_of_drivers
from race_schedule.update_race_schedule_table import update_the_race_schedule

# checks if the RACE_SCHEDULE, CONSTRUCTORSTANDINGS AND DRIVERSTANDINGS
# needs updating table # if so calls the relevant apis


def check_update_standings_and_schedule():
    last_completed_race = get_last_completed_race_date()
    max_date_in_standings = get_date_in_driver_standings()
    next_race = get_next_race_date()
    if next_race is None:
        update_the_race_schedule()

    if max_date_in_standings is None or max_date_in_standings < last_completed_race:
        update_the_standings_of_drivers()
        update_the_standings_of_constructors()
    elif max_date_in_standings is not None and max_date_in_standings > last_completed_race:
        return
    else:
        return
