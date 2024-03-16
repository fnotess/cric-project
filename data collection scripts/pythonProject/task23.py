import csv

import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt

# Read the CSV file with URLs
csv_file = 'odi_match_results_1980_to_2022.csv'
urls_df = pd.read_csv(csv_file)
print(urls_df)

# Define the CSV file to continuously append player details
output_csv = 'output_player_details_final.csv'

# Loop through each URL in the dataframe and continuously append player details to the file
for index, row in urls_df.iterrows():
    url = row['Scorecard Link']
    team1 = row['Team 1']
    team2 = row['Team 2']
    winner = row['Winner']
    margin = row['Margin']
    ground = row['Ground']
    matchDate = row['Match Date']
    scorecard = row['Scorecard']
    print(url)

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all 'a' tags with class 'ds-inline-flex ds-items-start ds-leading-none'
        player_links = soup.find_all('a', class_='ds-inline-flex ds-items-start ds-leading-none', href=lambda x: x and '/cricketers/' in x)

        for link in player_links:
            # Extract player name from 'title' attribute
            player_name = link.get('title')

            # Extract player ID from the last part of 'href' attribute
            player_id = link.get('href').split('-')[-1]

            # Open the CSV file in append mode and write the player details
            with open(output_csv, 'a', newline='') as file:
                print('appending to file')
                writer = csv.writer(file)
                writer.writerow([player_name, player_id, url, team1, team2, winner, ground, margin, matchDate, matchDate, scorecard])

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code} for URL: {url}")

print(f"Player details written to {output_csv}")