"""
This script collects hourly weather data for Chicago from the Open-Meteo API.
It retrieves data for the period from January 2024 to February 2024.
The collected data is then saved to a CSV file for further analysis. 
"""

# Import libraries
import pandas as pd
import requests

# Define the URL for the weather data API
url = "https://archive-api.open-meteo.com/v1/archive"

# Define the file path
path = r"C:\Users\wodnj\OneDrive\바탕 화면\DePaul Univ\24&25-02 Winter\Mining Big Data\CSC 555 - Final Project\Data File\2024_chicago_hourly_weather_from_january_to_february.csv"

# Define the parameters for the API request
params = {"latitude": 41.8781,
          "longitude": -87.6298,
          "start_date": "2024-01-01",
          "end_date": "2024-12-31",
          "hourly": ["temperature_2m",
                     "relative_humidity_2m",
                     "precipitation",
                     "windspeed_10m",
                     "apparent_temperature",
                     "windgusts_10m",
                     "weathercode"],
          "timezone": "America/Chicago"}

# Send a GET request to the API
response = requests.get(url, params = params)

# Check if the API request was successful
if response.status_code == 200:
    data = response.json() # Parse the JSON response from the API
    df = pd.DataFrame(data["hourly"]) # Convert the daily weather data into a pandas DataFrame
    df.to_csv(path, index = False) # Save the DataFrame to a CSV file
    print(f"File saved successfully: {path}")

else:
    print(f"API request failed: {response.status_code}, Response: {response.text}")
