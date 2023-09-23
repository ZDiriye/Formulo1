import pandas as pd
import plotly.graph_objects as go
from database_engine.engine import get_database_engine

# creates line and bar graph given driver id


def create_line_and_bar_graph(driver_id):
    engine = get_database_engine()
    
    with engine.connect() as connection:
        query = f"SELECT Round, Points FROM DRIVER_FORM WHERE DriverID = '{driver_id}' AND Date = (SELECT MAX(Date) FROM DRIVER_FORM WHERE DriverID  = '{driver_id}')"
        df = pd.read_sql_query(query, connection)


    # remove duplicate rounds and keep the last occurrence
    df = df.drop_duplicates(subset='Round', keep='last')

    df['TotalPoints'] = df['Points'].cumsum()

    fig = go.Figure()

    # add bar graph for points per round with custom hover text
    fig.add_trace(
        go.Bar(
            x=df['Round'],
            y=df['Points'],
            name='Round Points',
            hovertemplate='Round Points: %{y}<br>Round: %{x}<extra></extra>',
        ))

    # add line graph for cumulative total points
    fig.add_trace(
        go.Scatter(
            x=df['Round'],
            y=df['TotalPoints'],
            mode='lines+markers',
            name='Season Points',
            hovertemplate='Season Points: %{y}<br>Round: %{x}<extra></extra>'
        ))

    fig.update_layout(
        title='Season and Round Points:',
        xaxis_title='Round',
        yaxis_title='Points',
        legend=dict(x=0, y=1),
        width=320,
        height=425,
    )

    return fig.to_html()
