import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt

# Read the CSV file with URLs
csv_file = 'odi_match_results_1980_to_2022.csv'
urls_df = pd.read_csv(csv_file)
print(urls_df)

# Initialize an empty dataframe
columns = ['PlayerName', 'ID', 'url', 'team1', 'team2', 'winner', 'margin', 'ground', 'matchDate','matchDate2', 'scorecard']
all_player_df = pd.DataFrame(columns=columns)
print(all_player_df)

# Loop through each URL in the dataframe
for index, row in urls_df.iterrows():
    url = row['Scorecard Link']  # Assuming 'URL' is the column name in your CSV containing the URLs
    team1 = row['Team 1']
    team2 =  row['Team 2']
    winner = row['Winner']
    margin = row['Margin']
    ground = row['Ground']
    matchDate = row['Match Date']
    scorecard = row['Scorecard']
    print(url)

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Initialize an empty dataframe for each URL
        player_df = pd.DataFrame(columns=columns)

        # Find all 'a' tags with class 'ds-inline-flex ds-items-start ds-leading-none'
        player_links = soup.find_all('a', class_='ds-inline-flex ds-items-start ds-leading-none', href=lambda x: x and '/cricketers/' in x)

        for link in player_links:
            # Extract player name from 'title' attribute
            player_name = link.get('title')

            # Extract player ID from the last part of 'href' attribute
            player_id = link.get('href').split('-')[-1]

            # Parse match date and format it
            # try:
            #     match_date = dt.strptime(matchDate, "%b %d, %Y")
            #     formatted_match_date = match_date.strftime("%d+%b+%Y")
            # except ValueError:
            #     print(f"Error parsing match date: {matchDate}")
            #     continue

            # Check if the ID is already in the dataframe
            if player_id not in player_df['ID'].values:
                # Append the data to the dataframe
                player_df = pd.concat([player_df, pd.DataFrame({'PlayerName': [player_name], 'ID': [player_id], 'url': url,'team1': team1,'team2': team2,'winner': winner, 'ground' : ground, 'margin': margin,'matchDate' : matchDate,'matchDate2':matchDate, 'scorecard': scorecard})], ignore_index=True)

        # Append the player details for the current URL to the overall dataframe
        all_player_df = pd.concat([all_player_df, player_df], ignore_index=True)

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code} for URL: {url}")

# Display the overall dataframe with all player details
print(all_player_df)

# Write the final dataframe to a CSV file
output_csv = 'output_player_details.csv'
all_player_df.to_csv(output_csv, index=False)
print(f"Player details written to {output_csv}")
