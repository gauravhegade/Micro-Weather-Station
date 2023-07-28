import pandas as pd
import plotly.graph_objects as go
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
 
# Create the Dash app
app = dash.Dash("DASHBOARD", external_stylesheets=[dbc.themes.BOOTSTRAP])
 
# Define the layout
app.layout = html.Div([
    html.H1('Data Visualization'),
    
    html.Div([
        html.H2('Gauge Charts'),
        
        dcc.Graph(id='gauge-chart1'),
        dcc.Graph(id='gauge-chart2'),
        dcc.Graph(id='gauge-chart3'),
    ], style={'width': '50%', 'display': 'inline-block'}),
    
    html.Div([
        html.H2('Scatter Plots'),
        
        dcc.Graph(id='scatter-plot1'),
        dcc.Graph(id='scatter-plot2'),
        dcc.Graph(id='scatter-plot3'),
    ], style={'width': '50%', 'display': 'inline-block'}),
    
    dcc.Interval(
        id='interval-component',
        interval=10000,  # Update interval in milliseconds (10 seconds)
        n_intervals=0
    )
])
 
# Callback to update the charts
@app.callback(
    [Output('gauge-chart1', 'figure'),
     Output('gauge-chart2', 'figure'),
     Output('gauge-chart3', 'figure'),
     Output('scatter-plot1', 'figure'),
     Output('scatter-plot2', 'figure'),
     Output('scatter-plot3', 'figure')],
    [Input('interval-component', 'n_intervals')]
)
def update_charts(n):
    # Read the CSV file
    df = pd.read_csv('sensor_data.csv')
    
    # Create the gauge charts
    gauge_chart1 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=df['Temperature'].iloc[-1],
        title={'text': "Temperature"},
    ))
    gauge_chart2 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=df['Humidity'].iloc[-1],
        title={'text': "Humidity"},
    ))
    gauge_chart3 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=df['Range'].iloc[-1],
        title={'text': "Range"},
    ))
    
    # Create the scatter plots
    scatter_plot1 = go.Figure(go.Scatter(
        x=df['DateTime'],
        y=df['Temperature'],
        mode='markers',
        marker=dict(size=8),
    ))
    scatter_plot1.update_layout(title='Temperature')
 
    scatter_plot2 = go.Figure(go.Scatter(
        x=df['DateTime'],
        y=df['Humidity'],
        mode='markers',
        marker=dict(size=8),
    ))
    scatter_plot2.update_layout(title='Humidity')
 
 
    scatter_plot3 = go.Figure(go.Scatter(
        x=df['DateTime'],
        y=df['Range'],
        mode='markers',
        marker=dict(size=8),
    ))
    scatter_plot3.update_layout(title='Range')
    
    return gauge_chart1, gauge_chart2, gauge_chart3, scatter_plot1, scatter_plot2, scatter_plot3
 
# Run the app
if __name__ == '__main__':
    app.run_server()
