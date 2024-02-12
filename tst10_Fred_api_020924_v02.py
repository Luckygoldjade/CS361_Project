# Description: Fred_api
import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime
# import pandas as pd

def Fred_api(series_id, date_start, date_end):
    # Define the API key
    api_key = '21825ca1ead40bfc046ec885e67d3cb8'

    # Define the URL and return json data
    url = f'https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={api_key}&observation_start={date_start}&observation_end={date_end}&file_type=json'

    # Send the GET request
    response = requests.get(url)

    # Check if request was successful
    if response.status_code != 200:
        print("Failed to retrieve data.")
        return

    # Convert the response to JSON
    try:
        json_data = response.json()
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        return

    # Extract dates and values from the JSON data
    try:
        # Try to extract dates and values from the JSON data
        dates = []  # Create an empty list to store dates
        values = []  # Create an empty list to store values

        # Iterate over each entry in the 'observations' list
        for entry in json_data['observations']:
            # Try to extract the date from the entry and convert it to a datetime object
            try:
                date = datetime.strptime(entry['date'], '%Y-%m-%d')
            except ValueError:  # Handle the case where the date format is invalid
                print("Error extracting date from JSON entry")
                return

            # Try to extract the value from the entry and convert it to a float
            try:
                value = float(entry['value'])
            except ValueError:  # Handle the case where the value format is invalid
                print("Error extracting value from JSON entry")
                return

            # Append the date and value to their respective lists
            dates.append(date)
            values.append(value)

    except KeyError:  # Handle the case where the 'observations' key is missing in the JSON data
        print("Error: 'observations' key not found in JSON data")
        return
    except Exception as e:  # Handle any other unexpected errors
        print("Error:", e)
        return

    # Create a line plot using Matplotlib
    plt.figure(figsize=(10, 6))
    plt.plot(dates, values, marker='o', linestyle='-')

    # Set the title and labels
    plt.title(f'{treasury_rate} Treasury Rate')
    plt.xlabel('Date')
    plt.ylabel('Rate (%)')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Show the plot
    plt.show()
    # --



    # Pretty print the data
    print(json.dumps(json_data, indent=4))







if __name__ == "__main__":
    date_start = '2023-02-09'
    date_end = '2024-02-09'

    series_id = 'GS10'
    Fred_api(series_id=)    # 10 year treasury rate daily


    # Fred_api('GS2')     # 2 year treasury rate daily


    # Fred_api('GS5')     # 5 year treasury rate daily


    # Fred_api('GS20')    # 20 year treasury rate daily


    # Fred_api('GS30')    # 30 year treasury rate daily


