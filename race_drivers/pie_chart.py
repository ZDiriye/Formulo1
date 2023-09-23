import pandas as pd
import plotly.express as px
from database_engine.engine import get_database_engine

# creates pie chart given driver id


def create_pie_chart(driver_id):
    engine = get_database_engine()
    
    with engine.connect() as connection:
        query = f"SELECT Position, COUNT(*) as PositionCount FROM DRIVER_FORM WHERE DriverID = '{driver_id}' AND Date = (SELECT MAX(Date) FROM DRIVER_FORM WHERE DriverID = '{driver_id}') GROUP BY Position"
        df = pd.read_sql_query(query, connection)
  

    # filter out positions with zero counts and sort by position
    df = df[df["PositionCount"] > 0]
    df = df.sort_values(by='Position', ascending=True)

    # ceate hover text and position labels for the pie chart
    df['hover_text'] = (
        'Finished ' + df['PositionCount'].astype(str) +
        ' Time(s) In P' + df['Position']
    )
    df['PositionLabel'] = 'P' + df['Position']

    # create a pie chart using Plotly Express
    fig_pie = px.pie(
        df,
        names="PositionLabel",
        values="PositionCount",
        title='Finished Positions:',
        hole=0.4,
        custom_data=["hover_text"],
        hover_name="PositionLabel",
        template="plotly",
        width=320,
        height=425,
    )

    # customize pie chart appearance and hover information
    fig_pie.update_traces(
        hovertemplate="%{customdata[0]}",
        textinfo='none',
        marker=dict(colors=px.colors.qualitative.Plotly),
    )

    fig_pie_html = fig_pie.to_html(full_html=False)

    return fig_pie_html
