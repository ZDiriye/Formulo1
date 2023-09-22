import git
from flask import Flask, render_template, request
from update_race_standings_during_season import check_update_standings_during_season
from update_race_standings_schedule_new_season import check_update_schedule_standings_for_new_season
from update_driver_form_new_season import check_update_driver_form_new_season
from update_race_details_during_season import check_update_race_details_during_season
from race_details.winner_name_from_database import get_winner_name_from_database
from race_standings.driver_standings_from_database import get_driver_standings_from_database
from race_standings.constructor_standings_from_database import get_constructor_standings_from_database
from fastest_lap.fastest_lap_from_database import get_fastest_lap_from_database
from race_details.race_details_from_database import get_race_details_from_database
from race_schedule.race_schedule_from_database import get_race_schedule_from_database
from race_schedule.circuit_images_from_database import get_circuit_images_from_database
from race_schedule.country_images_from_database import get_country_images_from_database
from race_drivers.drivers_images_from_database import get_drivers_images_from_database
from update_driver_form_during_season import check_update_driver_form_during_season
from race_drivers.driver_form_from_database import get_driver_form_from_database
from race_drivers.driver_image_by_id import get_driver_image_by_id
from race_drivers.driver_image_by_name import get_driver_image_by_name
from race_teams.team_images_from_database import get_team_images_from_database
from race_drivers.pie_chart import create_pie_chart
from race_schedule.next_race_data_from_database import get_next_race_data_from_database
from race_drivers.drivers_championship_position import get_drivers_championship_position
from race_drivers.line_and_bar_graph import create_line_and_bar_graph
from race_schedule.race_from_database import get_race_from_database
from race_schedule.round_from_race_schedule import get_round_from_race_schedule
from race_schedule.check_is_race_completed import is_race_completed
from race_teams.official_team_images_from_database import get_official_team_images_from_database
from update_team_form_during_season import check_update_team_form_during_season
from update_driver_form_new_season import check_update_driver_form_new_season
from race_teams.team_form_from_database import get_team_form_from_database
from race_teams.official_team_images_by_id import get_official_team_image_by_id
from race_teams.teams_championship_position import get_teams_championship_position
from race_teams.driver_lineup_from_database import get_driver_lineup_from_database

app = Flask(__name__)

@app.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('./Formulo1')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400


@app.route("/")
def home():

    check_update_schedule_standings_for_new_season()
    check_update_standings_during_season()

    drivers_standings = get_driver_standings_from_database()
    constructors_standings = get_constructor_standings_from_database()

    team_images = get_team_images_from_database()
    country_images = get_country_images_from_database()

    next_race_dict = get_next_race_data_from_database()

    drivers_standings_dict = drivers_standings.to_dict(
        orient="records")
    constructors_standings_dict = constructors_standings.to_dict(
        orient="records")
    team_images_dict = team_images.to_dict(
        orient="records")
    country_images_dict = country_images.to_dict(
        orient="records")

    return render_template(
        'index.html',
        constructors_standings_dict=constructors_standings_dict,
        drivers_standings_dict=drivers_standings_dict,
        next_race_dict=next_race_dict,
        team_images_dict=team_images_dict,
        country_images_dict=country_images_dict
        )

@app.route("/races")
def races():

    check_update_schedule_standings_for_new_season()
    check_update_standings_during_season()

    race_schedule = get_race_schedule_from_database()
    circuit_images = get_circuit_images_from_database()

    race_schedule_dict = race_schedule.to_dict(orient="records")
    circuit_images_dict = circuit_images.to_dict(orient="records")

    return render_template(
        'races.html',
        race_schedule_dict=race_schedule_dict,
        circuit_images_dict=circuit_images_dict,
        )

@app.route('/races/<race_name>')
def race_details(race_name):

    round_num = get_round_from_race_schedule(race_name)
    next_race_dict = get_next_race_data_from_database()

    if is_race_completed(round_num):
        check_update_race_details_during_season(race_name, round_num)

        winner_driver_name_dict = get_winner_name_from_database(race_name)
        winner_driver_name = winner_driver_name_dict['DriverName']
        winner_drivers_image_dict = get_driver_image_by_name(winner_driver_name)
        
        fastest_lap_data_dict = get_fastest_lap_from_database(race_name)
        fastest_driver_name = fastest_lap_data_dict['Driver']
        fastest_drivers_image_dict = get_driver_image_by_name(fastest_driver_name)

        race_details_data = get_race_details_from_database(race_name) 

        country_images_data = get_country_images_from_database()
    
        country_images_dict = country_images_data.to_dict(
            orient="records")
        race_details_data_dict = race_details_data.to_dict(
            orient="records")

        return render_template(
            'completed_race_details.html',
            race_name=race_name,
            winner_driver_name=winner_driver_name,
            winner_drivers_image_dict=winner_drivers_image_dict,
            fastest_lap_data_dict=fastest_lap_data_dict,
            race_details_data_dict=race_details_data_dict,
            fastest_drivers_image_dict=fastest_drivers_image_dict,
            country_images_dict=country_images_dict,
            next_race_dict=next_race_dict,
            )
    else:
        race_data_dict = get_race_from_database(round_num)

        return render_template(
            'upcoming_race_details.html',
            race_data_dict=race_data_dict
            )

@app.route("/drivers")
def drivers():
        
    check_update_schedule_standings_for_new_season()
    check_update_standings_during_season()

    drivers_standings = get_driver_standings_from_database()
    driver_images = get_drivers_images_from_database()

    drivers_standings_dict = drivers_standings.to_dict(
        orient="records")
    driver_images_dict = driver_images.to_dict(
        orient="records")

    return render_template(
        'drivers.html',
        driver_images_dict=driver_images_dict,
        drivers_standings_dict=drivers_standings_dict,
        )

@app.route('/drivers/<driver_id>')
def drivers_form(driver_id):
        
    check_update_driver_form_new_season(driver_id)
    check_update_driver_form_during_season(driver_id)

    driver_form = get_driver_form_from_database(driver_id)
    combined_graph_html = create_line_and_bar_graph(driver_id)
    fig_pie_html = create_pie_chart(driver_id)

    championship_position_dict = get_drivers_championship_position(driver_id)
    drivers_image_dict = get_driver_image_by_id(driver_id)
    next_race_dict = get_next_race_data_from_database()

    driver_form_dict = driver_form.to_dict(
        orient="records")

    return render_template(
        'drivers_form.html',
        driver_form_dict=driver_form_dict,
        fig_pie_html=fig_pie_html,
        combined_graph_html=combined_graph_html,
        championship_position_dict=championship_position_dict,
        drivers_image_dict=drivers_image_dict,
        next_race_dict=next_race_dict
        )

@app.route("/teams")
def teams():
        
    check_update_schedule_standings_for_new_season()
    check_update_standings_during_season()

    constructor_standings = get_constructor_standings_from_database()
    official_team_images = get_official_team_images_from_database()

    constructor_standings_dict = constructor_standings.to_dict(
        orient="records")
    official_team_images_dict = official_team_images.to_dict(
        orient="records")

    return render_template(
        'teams.html',
        constructor_standings_dict=constructor_standings_dict,
        official_team_images_dict=official_team_images_dict
        )

@app.route('/teams/<constructor_id>')
def teams_form(constructor_id):

    check_update_driver_form_new_season(constructor_id)
    check_update_team_form_during_season(constructor_id)

    team_form = get_team_form_from_database(constructor_id)

    championship_position_dict = get_teams_championship_position(constructor_id)
    official_teams_image_dict = get_official_team_image_by_id(constructor_id)
    next_race_dict = get_next_race_data_from_database()
    driver_lineup_dict = get_driver_lineup_from_database(constructor_id)
    driver1_name = driver_lineup_dict["DriverName1"]
    driver2_name = driver_lineup_dict["DriverName2"]
    drivers1_image_dict = get_driver_image_by_name(driver1_name)
    drivers2_image_dict = get_driver_image_by_name(driver2_name)

    team_form_dict = team_form.to_dict(
        orient="records")

    return render_template(
        'teams_form.html',
        team_form_dict=team_form_dict,
        driver1_name=driver1_name,
        driver2_name=driver2_name,
        drivers1_image_dict=drivers1_image_dict,
        drivers2_image_dict=drivers2_image_dict,
        championship_position_dict=championship_position_dict,
        official_teams_image_dict=official_teams_image_dict,
        next_race_dict=next_race_dict
        )   

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
