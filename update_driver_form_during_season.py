from race_drivers.update_driver_form_table import update_the_form_of_drivers
from race_schedule.last_completed_race_date import get_last_completed_race_date
from race_drivers.date_in_driver_form_table import get_date_in_driver_form_table

# checks if the DRIVER_FORM table needs updating


def check_update_driver_form_during_season(driver_id):
    last_completed_race = get_last_completed_race_date()
    date_in_driver_form = get_date_in_driver_form_table(driver_id)

    if date_in_driver_form is None or date_in_driver_form < last_completed_race:
        update_the_form_of_drivers(driver_id)
    elif date_in_driver_form is not None and date_in_driver_form > last_completed_race:
        return
    else:
        return
