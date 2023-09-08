from race_drivers.update_current_form_table import update_the_current_form_of_drivers
from race_schedule.last_completed_race_date import get_last_completed_race_date
from race_schedule.update_race_schedule_table import update_the_race_schedule
from race_drivers.date_in_current_form_table import get_date_in_current_form_table
from race_schedule.next_race_date import get_next_race_date
# checks if the RACE_SCHEDULE and CURRENT_FORM table needs updating, 
# if so calls the relevant apis


def check_update_current_form(driver_id):
    last_completed_race = get_last_completed_race_date()
    date_in_current_form = get_date_in_current_form_table(driver_id)
    next_race = get_next_race_date
    if next_race is None:
        update_the_race_schedule()

    if date_in_current_form is None or date_in_current_form < last_completed_race:
        update_the_current_form_of_drivers(driver_id)
    elif date_in_current_form is not None and date_in_current_form > last_completed_race:
        return
    else:
        return
