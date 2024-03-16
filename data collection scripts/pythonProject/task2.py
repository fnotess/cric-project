import requests
from bs4 import BeautifulSoup
import pandas as pd

# https://stats.espncricinfo.com/ci/engine/player/253802.html?class=2;type=allround
# https://stats.espncricinfo.com/ci/engine/player/6502.html?class=2;spanmax1=13+Jan+1980;spanval1=span;template=results;type=allround

url = 'https://www.espncricinfo.com/series/benson-hedges-world-series-cup-1979-80-60807/australia-vs-england-10th-match-65295/full-scorecard'

# Fetch the HTML content from the URL
response = requests.get(url)
html_code = response.content

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_code, 'html.parser')

# Extract player names from BATTING section
batting_table = soup.find('table', class_='ci-scorecard-table')
print(batting_table)
player_rows = batting_table.find_all('tr', class_='ds-table-row-compact-bottom')
print(player_rows)

player_data = []
for row in player_rows:
    player_name = row.find('a', class_='ds-inline-flex').text.strip()
    player_href = row.find('a', class_='ds-inline-flex')['href']
    country = row.find('span', class_='ds-text-tight-xs').text.strip()
    player_data.append({'Name': player_name, 'Href': player_href, 'Country': country})

# Extract player names from 'DID NOT BAT' section (if available)
did_not_bat_row = soup.find('tr', class_='ds-table-row-compact-top')
if did_not_bat_row:
    did_not_bat_names = did_not_bat_row.find('div', class_='ds-text-tight-s').text.strip().split(',')
    for name in did_not_bat_names:
        player_data.append({'Name': name.strip(), 'Href': None, 'Country': None})

# Create DataFrame
df = pd.DataFrame(player_data)

# Display the DataFrame
print(df)
