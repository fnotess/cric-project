import requests
from bs4 import BeautifulSoup
import pandas as pd

# Replace the URL with the actual URL of the HTML page you want to scrape
url = 'https://www.espncricinfo.com/series/benson-hedges-world-series-cup-1979-80-60807/australia-vs-england-10th-match-65295/full-scorecard'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Initialize an empty dataframe
    columns = ['PlayerName', 'ID']
    player_df = pd.DataFrame(columns=columns)

    # Find all 'a' tags with class 'ds-inline-flex ds-items-start ds-leading-none'
    player_links = soup.find_all('a', class_='ds-inline-flex ds-items-start ds-leading-none',href=lambda x: x and '/cricketers/' in x)

    for link in player_links:
        # Extract player name from 'title' attribute
        player_name = link.get('title')
        print(player_name)

        # Extract player ID from the last part of 'href' attribute
        player_id = link.get('href').split('-')[-1]
        print(player_id)

        # Check if the ID is already in the dataframe
        if player_id not in player_df['ID'].values:
            # Append the data to the dataframe
            print('k')
            player_df = pd.concat([player_df, pd.DataFrame({'PlayerName': [player_name], 'ID': [player_id]})],
                                  ignore_index=True)
            #player_df = player_df.append({'PlayerName': player_name, 'ID': player_id}, ignore_index=True)

    # Display the dataframe
    print(player_df)

    # Now you have a dataframe with unique player names and IDs
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
