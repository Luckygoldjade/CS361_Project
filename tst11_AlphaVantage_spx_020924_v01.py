import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime
# import pandas as pd




def AlphaVantage_api(symbol, date_start, date_end):
    # Define the API key
    api_key = '3WXQQNRV69AIGYE7'

    # Define the URL and return json data
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={api_key}'

    response = requests.get(url)
    data = response.json()

    # The 'data' variable contains the JSON data from the AlphaVantage API.
    # 'Time Series (Daily)' is a key in this JSON data that contains daily stock data.

    # First, we want to get all the dates for which we have stock data.
    # The dates are the keys in the 'Time Series (Daily)' dictionary.
    # We use a list comprehension to create a list of these dates, converting them to datetime objects as we go.
    dates = []
    for date_str in data['Time Series (Daily)'].keys():
        date = datetime.strptime(date_str, "%Y-%m-%d")  # Convert the date string to a datetime object

        # Save dates within date_start and date_end
        dates.append(date)

    # Next, we want to get the closing price for each of these dates.
    # The closing price is stored in the '4. close' key in the dictionary for each date.
    # Again, we use a list comprehension to create a list of these closing prices, converting them to floats as we go.
    closing_prices = []
    for date in dates:
        date_str = date.strftime('%Y-%m-%d')  # Convert the datetime object back to a string
        closing_price = float(data['Time Series (Daily)'][date_str]['4. close'])  # Get the closing price and convert it to a float
        
        # Save closing prices within date_start and date_end
        closing_prices.append(closing_price)

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(dates, closing_prices, marker='o', linestyle='-')

    # Set the title and labels
    plt.title('Stock Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Show the plot
    plt.tight_layout()
    plt.show()






    # Pretty print the data
    print(json.dumps(data, indent=4))

if __name__ == "__main__":
    symbol = 'SPY'
    date_start = '2023-02-09'
    date_end = '2024-02-09'
    AlphaVantage_api(symbol, date_start, date_end)
