from .constructor_standings_from_api import get_constructor_standings_from_api
from database_engine.engine import get_database_engine
from .parse_constructor_standings import parse_constructor_standings_data

# updates the constructor standings in the sql table CONSTRUCTORSTANDINGS


def update_the_standings_of_constructors():
    engine = get_database_engine()

    current_standings_data = get_constructor_standings_from_api()
    df = parse_constructor_standings_data(current_standings_data)
    with engine.connect() as connection:
        df.to_sql('CONSTRUCTORSTANDINGS', con=connection,
                  if_exists='append', index=False)
