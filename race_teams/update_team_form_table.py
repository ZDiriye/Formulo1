from database_engine.engine import get_database_engine
from .team_form_from_api import get_team_form_from_api
from .parse_team_form import parse_team_form_data

# updates the team form in the sql table TEAM_FORM


def update_the_form_of_teams(constructor_id):
    engine = get_database_engine()

    team_form_data = get_team_form_from_api(constructor_id)
    df = parse_team_form_data(team_form_data, constructor_id)
    with engine.connect() as connection:
        df.to_sql('TEAM_FORM', con=connection,
                  if_exists='append', index=False)
