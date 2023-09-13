from race_schedule.next_race_date import get_next_race_date
from race_standings.update_constructor_standings_table import update_the_standings_of_constructors
from race_standings.update_driver_standings_table import update_the_standings_of_drivers
from race_schedule.update_race_schedule_table import update_the_race_schedule

# checks if the RACE_SCHEDULE, CONSTRUCTORSTANDINGS AND DRIVERSTANDINGS
# needs reseting for the new season


def check_update_new_season():
    next_race = get_next_race_date()

    if next_race is None:
        update_the_race_schedule()
        update_the_standings_of_drivers()
        update_the_standings_of_constructors()


