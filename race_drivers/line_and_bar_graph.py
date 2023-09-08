import pandas as pd
import plotly.graph_objects as go
from database_engine.engine import get_database_engine

def create_line_and_bar_graph(driver_id):
    query = f"SELECT Round, Points FROM CURRENT_FORM WHERE DriverID = '{driver_id}'"
    engine = get_database_engine()
    conn = engine.connect()
    df = pd.read_sql_query(query, conn)
    conn.close()

    # Remove duplicate rounds and keep the last occurrence
    df = df.drop_duplicates(subset='Round', keep='last')

    df['TotalPoints'] = df['Points'].cumsum()

    fig = go.Figure()

    # Add bar graph for points per round with custom hover text
    fig.add_trace(
        go.Bar(
            x=df['Round'],
            y=df['Points'],
            name='Round Points',
            hovertemplate='Round Points: %{y}<br>Round: %{x}<extra></extra>',
        ))

    # Add line graph for cumulative total points
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
        width=341,
        height=425,
    )

    return fig.to_html()
