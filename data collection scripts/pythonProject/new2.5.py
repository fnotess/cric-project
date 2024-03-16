# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
#
# # Replace this with the URL of the page you want to scrape
# url = "https://www.espncricinfo.com/series/benson-hedges-world-series-cup-1979-80-60807/australia-vs-england-10th-match-65295/full-scorecard"
#
# # Send an HTTP GET request to the URL
# response = requests.get(url)
#
# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content of the page
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     # Find all elements with the specified class that contains player names
#     player_name_elements = soup.find_all('span', class='ds-text-tight-s ds-font-medium ds-text-typo ds-underline ds-decoration-ui-stroke hover:ds-text-typo-primary hover:ds-decoration-ui-stroke-primary ds-block ds-cursor-pointer')
#
#     # Extract player names and their respective countries
#     player_data = []
#     country = None
#
#     for player_element in player_name_elements:
#         # Check if the player name is within a "BOWLING" section and ignore it
#         if player_element.find_previous('th', text='BOWLING'):
#             continue
#
#         player_name = player_element.text.strip()
#         # Find the nearest country name for the player
#         country_element = player_element.find_previous('span', class='ds-text-title-xs ds-font-bold ds-capitalize')
#         if country_element:
#             country = country_element.text.strip()
#         player_data.append({'Player Name': player_name, 'Country': country})
#
#     # Create a DataFrame from the player data
#     df = pd.DataFrame(player_data)
#
#     # Print the DataFrame
#     print(df)
#
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")
