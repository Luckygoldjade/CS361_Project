# Description: Fred_api
import requests
import json
import plotly.graph_objects as go

def Fred_api(treasury_rate):
    # Define the API key and series ID
    api_key = '21825ca1ead40bfc046ec885e67d3cb8'
    series_id = treasury_rate

    # Define the URL
    url = f'https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={api_key}&file_type=json&real_time_start=2023-02-09&real_time_end=2024-02-09'

    # Send the GET request
    response = requests.get(url)

    # Convert the response to JSON
    data = response.json()



    # Convert the response to JSON format (dictionary in Python)
    data = response.json()

    # Extract dates and corresponding values from the JSON data
    dates = [entry['date'] for entry in data['observations']]  # Extracting dates
    values = [float(entry['value']) for entry in data['observations']]  # Extracting corresponding values

    # Create a scatter plot using Plotly
    fig = go.Figure(data=go.Scatter(x=dates, y=values))  # Creating a scatter plot

    # Update the layout of the plot (e.g., title, axis labels)
    fig.update_layout(title=f'{treasury_rate} Treasury Rate', xaxis_title='Date', yaxis_title='Rate (%)')

    # Show the plot
    fig.show()



    # # Pretty print the data
    # print(json.dumps(data, indent=4))







if __name__ == "__main__":
    # Fred_api('GS10')    # 10 year treasury rate daily
    Fred_api('GS2')     # 2 year treasury rate daily
    # Fred_api('GS5')     # 5 year treasury rate daily
    # Fred_api('GS20')    # 20 year treasury rate daily
    # Fred_api('GS30')    # 30 year treasury rate daily


