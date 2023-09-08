# Formulo 1

## Project Overview

Formulo 1 is a web application designed to provide users with real-time updates and information about Formula 1 racing. This application offers a user-friendly interface that allows users to access statistics related to Formula 1, including race standings, schedules, driver details, and more. By fetching data from various sources, including a database and external APIs, Formulo 1 keeps users informed about the latest racing events and statistical insights.

## Use Cases
1. **View Standings and Schedules**: Users can effortlessly access up-to-date driver and constructor standings, as well as a countdown to next Formula 1 race of the current season.

2. **Race Details**: The application provides comprehensive information about both completed and upcoming races. This includes detailed race results and fastest lap statistics for each circuit.

3. **Driver Information**: Users can explore profiles of individual drivers, including their current form, accompanied by insightful visualisations.

## Non-functional Requirements

- **Reliability**: Formulo 1 places a strong emphasis on data accuracy and reliability. The application actively fetches data from reliable sources to maintain the most accurate and up-to-date information.

- **Performance**: The application is designed to provide exceptional performance by efficiently rendering data and visual elements. Users can expect a seamless experience while navigating through the application.

## Functional Requirements

- **Home Page**: Upon visiting the home page, users are greeted with a an overview of essential information, including current driver and constructor standings, details about the upcoming race.

- **Race Schedule**: The race schedule section presents users with the complete calendar of Formula 1 races for the ongoing season. Users can easily identify the dates and locations of each race.

- **Race Details**: Formulo 1 provides in-depth insights into both completed and upcoming races. For completed races, users can explore detailed race results and race-specific statistics. For upcoming races, users can access information about the race name and scheduled date and time.

- **Driver Profiles**: Users have the opportunity to delve into detailed profiles of individual drivers. These profiles showcase current form and interactive visualisations.

## Data Sources and APIs

This project utilises the following data sources and APIs:

- **Ergast API:** This Formula 1 API provides race schedules, driver standings, constructor standings, race details, and other relevant data.
- **Database:** The project interacts with a Sqlite database to store and retrieve data efficiently. SQLAlchemy is used as the SQL toolkit and ORM.
- **Images:** Images of drivers, teams, and races are sourced from external sources and integrated into the web application.


## Access

Access the web application in your browser by visiting the domain name: http://formulo1.pythonanywhere.com
