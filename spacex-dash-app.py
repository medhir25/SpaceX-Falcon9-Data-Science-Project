import pandas as pd
import plotly.express as px

from dash import Dash, html, dcc
from dash.dependencies import Input, Output

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")

max_payload = spacex_df["Payload Mass (kg)"].max()
min_payload = spacex_df["Payload Mass (kg)"].min()

# Create a dash application
app = Dash(__name__)

# List of launch sites
launch_sites = spacex_df["Launch Site"].unique()

app.layout = html.Div(children=[
    html.H1(
        "SpaceX Launch Records Dashboard",
        style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}
    ),

    # TASK 1: Dropdown
    dcc.Dropdown(
        id='site-dropdown',
        options=[{'label': 'All Sites', 'value': 'ALL'}] +
                [{'label': site, 'value': site} for site in launch_sites],
        value='ALL',
        placeholder='Select a Launch Site',
        searchable=True
    ),

    html.Br(),

    # Pie Chart
    dcc.Graph(id='success-pie-chart'),

    html.Br(),

    html.P("Payload range (Kg):"),

    # TASK 3: Range Slider
    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=10000,
        step=1000,
        marks={i: str(i) for i in range(0, 10001, 1000)},
        value=[min_payload, max_payload]
    ),

    html.Br(),

    # Scatter Plot
    dcc.Graph(id='success-payload-scatter-chart')
])

# TASK 2: Pie Chart Callback
@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def get_pie_chart(entered_site):

    if entered_site == 'ALL':
        fig = px.pie(
            spacex_df.groupby('Launch Site')['class']
            .sum()
            .reset_index(),
            values='class',
            names='Launch Site',
            title='Total Successful Launches by Site'
        )
        return fig

    filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]

    fig = px.pie(
        filtered_df,
        names='class',
        title=f'Success vs Failure for {entered_site}'
    )

    return fig


# TASK 4: Scatter Plot Callback
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [
        Input('site-dropdown', 'value'),
        Input('payload-slider', 'value')
    ]
)
def get_scatter_chart(entered_site, payload_range):

    low, high = payload_range

    filtered_df = spacex_df[
        (spacex_df['Payload Mass (kg)'] >= low) &
        (spacex_df['Payload Mass (kg)'] <= high)
    ]

    if entered_site == 'ALL':

        fig = px.scatter(
            filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title='Payload vs Launch Outcome (All Sites)'
        )

        return fig

    filtered_df = filtered_df[
        filtered_df['Launch Site'] == entered_site
    ]

    fig = px.scatter(
        filtered_df,
        x='Payload Mass (kg)',
        y='class',
        color='Booster Version Category',
        title=f'Payload vs Launch Outcome for {entered_site}'
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)