import git
from flask import Flask, render_template, request
from check_update_race_standings_and_schedule import check_update_standings_and_schedule
from check_update_race_details import check_update_details
from race_standings.driver_standings_from_database import get_driver_standings_from_database
from race_standings.constructor_standings_from_database import get_constructor_standings_from_database
from fastest_lap.fastest_lap_from_database import get_fastest_lap_from_database
from race_details.race_details_from_database import get_race_details_from_database
from race_schedule.race_schedule_from_database import get_race_schedule_from_database
from race_schedule.race_images_from_database import get_race_images_from_database
from race_schedule.country_images_from_database import get_country_images_from_database
from race_drivers.drivers_images_from_database import get_drivers_images_from_database
from check_update_current_race_form import check_update_current_form
from race_drivers.current_form_from_database import get_current_form_from_database
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


app = Flask(__name__)

@app.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('./SEOProject')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400


@app.route("/")
def home():
        check_update_standings_and_schedule()

        drivers_standings_data = get_driver_standings_from_database()
        constructors_standings_data = get_constructor_standings_from_database()
        team_images_data = get_team_images_from_database()
        country_images_data = get_country_images_from_database()

        next_race_info = get_next_race_data_from_database()

        team_images = team_images_data.to_dict(
            orient="records")
        country_images = country_images_data.to_dict(
            orient="records")
        driver_standings_table = drivers_standings_data.to_dict(
            orient="records")
        constructor_standings_table = constructors_standings_data.to_dict(
            orient="records")

        return render_template(
            'index.html',
            constructor_standings_table=constructor_standings_table,
            driver_standings_table=driver_standings_table,
            next_race=next_race_info,
            team_images=team_images,
            country_images=country_images
            )

@app.route("/races")
def races():
        check_update_standings_and_schedule()

        schedule_data = get_race_schedule_from_database()
        race_images = get_race_images_from_database()

        race_images = race_images.to_dict(orient="records")
        schedule_data = schedule_data.to_dict(orient="records")

        return render_template(
            'races.html',
            schedule_data=schedule_data,
            race_images=race_images,
            )

@app.route('/races/<race_name>')
def race_details(race_name):
        round_num = get_round_from_race_schedule(race_name)
        next_race_info = get_next_race_data_from_database()

        # have to check if the first round is completed because the
        # api will return none if the round is not completed
        if is_race_completed(round_num):
            check_update_details(race_name, round_num)

            race_details_data = get_race_details_from_database(race_name) #just pass the name

            fastest_lap_data = get_fastest_lap_from_database(race_name)
            fastest_lap_data_info = {
                "Driver": fastest_lap_data["Driver"][0],
                "FastestLap": fastest_lap_data["FastestLap"][0],
            }
            driver_name = fastest_lap_data_info['Driver']

            drivers_image = get_driver_image_by_name(driver_name)
            drivers_image_info = {
                "ImagePath": drivers_image["ImagePath"][0],
                "DriverName": drivers_image["DriverName"][0],
            }
            country_images_data = get_country_images_from_database()
            
            country_images = country_images_data.to_dict(
                orient="records")
            race_details_table = race_details_data.to_dict(
                orient="records")

            return render_template(
                'completed_race_details.html',
                race_details_table=race_details_table,
                fastest_lap_data=fastest_lap_data_info,
                race_name=race_name,
                drivers_image_info=drivers_image_info,
                country_images=country_images,
                next_race=next_race_info
                )
        else:
            race_data = get_race_from_database(round_num)
            
            race_data_info = {
                "RaceName": race_data["RaceName"][0],
                "Datetime": race_data["Date"][0] + " " + race_data["Time"][0],
            }
            
            return render_template(
                'upcoming_race_details.html',
                race_data=race_data_info,
                next_race=next_race_info)

@app.route("/drivers")
def drivers():
        check_update_standings_and_schedule()

        drivers_standings_data = get_driver_standings_from_database()
        driver_images = get_drivers_images_from_database()

        drivers_standings = drivers_standings_data.to_dict(orient="records")
        driver_images = driver_images.to_dict(orient="records")

        return render_template(
            'drivers.html',
            driver_images=driver_images,
            drivers_standings=drivers_standings,
            )

@app.route('/drivers/<driver_id>')
def drivers_form(driver_id):
        check_update_current_form(driver_id)

        current_form = get_current_form_from_database(driver_id)
        combined_graph_html = create_line_and_bar_graph(driver_id)
        fig_pie_html = create_pie_chart(driver_id)
        next_race_info = get_next_race_data_from_database()

        championship_position = get_drivers_championship_position(driver_id)
        championship_position_data = {
            "Position": championship_position["Position"][0]
        }
        
        drivers_image = get_driver_image_by_id(driver_id)
        drivers_image_info = {
            "ImagePath": drivers_image["ImagePath"][0],
            "DriverName": drivers_image["DriverName"][0],
        }

        current_form = current_form.to_dict(orient="records")

        return render_template(
            'drivers_form.html',
            current_form=current_form,
            drivers_image_info=drivers_image_info,
            fig_pie_html=fig_pie_html,
            combined_graph_html=combined_graph_html,
            championship_position_data=championship_position_data,
            next_race=next_race_info
            )

@app.route("/teams")
def teams():
        check_update_standings_and_schedule()

        constructor_standings_data = get_constructor_standings_from_database()
        team_images = get_team_images_from_database()

        constructor_standings = constructor_standings_data.to_dict(orient="records")
        team_images = team_images.to_dict(orient="records")

        return render_template(
            'teams.html',
            team_images=team_images,
            constructor_standings=constructor_standings,
            )

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
