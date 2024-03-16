import requests
from bs4 import BeautifulSoup
import re

# Define the URL of the cricket scorecard
url = "https://www.espncricinfo.com/series/benson-hedges-world-series-cup-1979-80-60807/australia-vs-england-10th-match-65295/full-scorecard"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the player names using regular expressions
    player_name_pattern = re.compile(r'"slug":"\w+","\nameFull":"(.*?)"')
    player_names = [match.group(1) for match in player_name_pattern.finditer(str(soup))]

    # The player names are listed in pairs for the two teams, so we split them accordingly
    team1_players = player_names[:11]
    team2_players = player_names[11:]

    # Print the player names for both teams
    print("Team 1 Players:")
    for idx, player in enumerate(team1_players, start=1):
        print(f"{idx}. {player}")

    print("\nTeam 2 Players:")
    for idx, player in enumerate(team2_players, start=1):
        print(f"{idx}. {player}")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
