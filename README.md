# Formulo 1

## Project Overview

Formulo 1 is a web application designed to provide users with real-time updates and information about Formula 1 racing. This application offers a user-friendly interface that allows users to access statistics related to Formula 1, including race standings, schedules, race details and current driver's and team's form. Formulo 1 keeps users informed about the latest racing events and statistical insights.

## Use Cases
1. **View Current Standings and Countdown To Next Race**: Users can effortlessly access up-to-date driver and constructor standings, as well as a countdown to next Formula 1 race of the current season.

2. **View Races In The Current Season**: Users can look at different races and choose the one for which they want to see the statistics.

3. **Analyse Race details**: The application provides comprehensive information about both completed and upcoming races. This includes detailed standings, race winner and fastest lap statistics for each circuit.

4. **View Drivers In The Current Season**: Users can look at individual drivers and choose which driver statistics they want to see.

5. **Analyse a Driver's Form**: The application gives detailed information regarding the chosen driver's form. This shows each driver's current championship position, number of race wins, track record, and detailed information on their completed race performances.

6. **View Teams In The Current Season**: Users can look at individual teams and choose which team statistics they want to see.

7. **Analyse a Team's Form**: The application provides thorough information about the chosen team's form. This displays each team's current championship position, driver lineup, and information on the team's completed race performances.


## Non-functional Requirements

- **Reliability**: Formulo 1 places a strong emphasis on data accuracy and reliability. The application actively fetches data from reliable sources to maintain the most accurate and up-to-date information.

- **Performance**: The application is designed to provide exceptional performance by efficiently rendering data and visual elements. Users can expect a seamless experience while navigating through the application.

## Functional Requirements

1. **View Current Standings and Countdown To Next Race**: This information is fetched and updated through functions like check_update_standings_during_season() and get_next_race_data_from_database().

2. **View Races In The Current Season**: The race schedule and circuit images are retrieved and displayed using functions such as get_race_schedule_from_database() and get_circuit_images_from_database().

3. **Analyse Race details**:  Race details are updated using functions like check_update_race_details_during_season() and fetched from the database through functions like get_race_details_from_database().

4. **View Drivers In The Current Season**: Driver standings and images are fetched from the database using functions like get_driver_standings_from_database() and get_drivers_images_from_database().

5. **Analyse a Driver's Form**: Driver form data is fetched and updated through functions like check_update_driver_form_new_season() and check_update_driver_form_during_season().

6. **View Teams In The Current Season**: . Constructor standings and official team images are retrieved from the database using functions like get_constructor_standings_from_database() and get_official_team_images_from_database().

7. **Analyse a Team's Form**:  Team form data is updated through functions like check_update_team_form_during_season() and fetched using get_team_form_from_database().

## Data Sources and APIs

This project utilises the following data sources and APIs:

- **Ergast API:** This Formula 1 API provides the data needed to build Formulo1.
- **Database:** The project interacts with a Sqlite database to store data from the api into structured tables and also uses SQL to query specific data from these tables.
- **Images:** Images of drivers, teams, and races are sourced from external sources and integrated into the web application.


## Access

Access the web application in your browser by visiting the domain name: http://formulo1.pythonanywhere.com
