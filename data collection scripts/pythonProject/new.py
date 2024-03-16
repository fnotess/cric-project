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

    # Find all elements with the specified class that contains player names
    player_name_elements = soup.find_all('span', class_='ds-text-tight-s ds-font-medium ds-text-typo ds-underline ds-decoration-ui-stroke hover:ds-text-typo-primary hover:ds-decoration-ui-stroke-primary ds-block ds-cursor-pointer')

    # Extract player names from the elements
    player_names = [element.text.strip() for element in player_name_elements]

    # Find the "Did not bat" section and extract names (with error handling)
    did_not_bat_section = soup.find("div", text="Did not bat:")
    did_not_bat_names = []
    if did_not_bat_section:
        did_not_bat_names = [name.text.strip() for name in did_not_bat_section.find_all('span', class_='ds-text-tight-s ds-font-medium ds-text-typo ds-underline ds-decoration-ui-stroke hover:ds-text-typo-primary hover:ds-decoration-ui-stroke-primary ds-block ds-mr-1 ds-cursor-pointer')]

    # Print the extracted player names
    print("Player Names:")
    for name in player_names:
        print(name)

    # Print the "Did not bat" names
    print("\nDid not bat:")
    for name in did_not_bat_names:
        print(name)

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
