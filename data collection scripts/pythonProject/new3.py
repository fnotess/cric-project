import requests
from bs4 import BeautifulSoup

# Replace this with the URL of the page you want to scrape
url = "https://www.espncricinfo.com/series/benson-hedges-world-series-cup-1979-80-60807/australia-vs-england-10th-match-65295/full-scorecard"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the "BATTING" header
    batting_header = soup.find('th', class_='ds-w-0 ds-whitespace-nowrap ds-min-w-max ds-text-left', text='BATTING')

    if batting_header:
        # Find the parent table containing player names
        batting_table = batting_header.find_parent('table')

        # Find all elements with the specified class that contains player names
        player_name_elements = batting_table.find_all('span', class_='ds-text-tight-s ds-font-medium ds-text-typo ds-underline ds-decoration-ui-stroke hover:ds-text-typo-primary hover:ds-decoration-ui-stroke-primary ds-block ds-cursor-pointer')

        # Extract player names
        player_names = [element.text.strip() for element in player_name_elements]

        # Print the extracted player names
        print("Player Names:")
        for name in player_names:
            print(name)

    else:
        print("BATTING header not found in the HTML.")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
