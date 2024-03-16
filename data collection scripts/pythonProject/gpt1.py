from bs4 import BeautifulSoup
import requests

url = "https://www.espncricinfo.com/series/benson-hedges-world-series-cup-1979-80-60807/australia-vs-england-10th-match-65295/full-scorecard"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# Create an empty list to store the player names and their countries
player_data = []

# Find the batting table for Australia
australia_batting_table = soup.find('table', class_='ci-scorecard-table')

# Loop through the rows in the Australia batting table
try:
    for row in australia_batting_table.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) > 0:
            player_name = cells[0].find('a').text.strip()
            player_country = 'Australia'
            player_data.append((player_name, player_country))
    
except AttributeError:
    pass

# Find the "Did not bat" section for Australia and extract player names
did_not_bat_section = soup.find('div', class_='ds-font-regular', text='Did not bat:')
if did_not_bat_section:
    did_not_bat_players = [player.text.strip() for player in did_not_bat_section.find_all('a')]
    player_data.extend([(player, 'Australia') for player in did_not_bat_players])

# Find the batting table for England
try:
    england_batting_table = australia_batting_table.find_next('table', class_='ci-scorecard-table')
    # Loop through the rows in the England batting table
    for row in england_batting_table.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) > 0:
            player_name = cells[0].find('a').text.strip()
            player_country = 'England'
            player_data.append((player_name, player_country))
except AttributeError:
    pass

# Find the "Did not bat" section for Australia and extract player names
did_not_bat_section = soup.find('div', class_='ds-font-regular', text='Did not bat:')
print(did_not_bat_section)
if did_not_bat_section:
    did_not_bat_players = [player.text.strip() for player in did_not_bat_section.find_all('a')]
    player_data.extend([(player, 'England') for player in did_not_bat_players])

# Print the scraped player data
for player, country in player_data:
    print(f"Player: {player}, Country: {country}")
