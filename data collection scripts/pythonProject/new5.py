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
#     # Find all "BATTING" headers
#     batting_headers = soup.find_all('th', class_='ds-w-0 ds-whitespace-nowrap ds-min-w-max ds-text-left', text='BATTING')
#
#     if batting_headers:
#         # Initialize lists to store player data
#         player_data = []
#
#         for batting_header in batting_headers:
#             # Find the parent table containing player names
#             batting_table = batting_header.find_parent('table')
#
#             # Find all elements with the specified class that contains player names
#             player_name_elements = batting_table.find_all('span', class=['ds-text-tight-s', 'ds-font-medium', 'ds-text-typo', 'ds-underline', 'ds-decoration-ui-stroke', 'hover:ds-text-typo-primary', 'hover:ds-decoration-ui-stroke-primary', 'ds-block', 'ds-cursor-pointer'])
#
#             # Extract player names and their respective countries
#             player_country = batting_table.find_previous('span', class='ds-text-title-xs ds-font-bold ds-capitalize').text.strip()
#
#             for element in player_name_elements:
#                 player_name = element.text.strip()
#                 player_data.append({'Player Name': player_name, 'Country': player_country})
#
#         # Find the "Did not bat" section and extract names
#         did_not_bat_section = soup.find('strong', text='Did not bat:')
#         if did_not_bat_section:
#             did_not_bat_names = did_not_bat_section.find_next('a', class=['ds-text-tight-s', 'ds-font-medium', 'ds-text-typo', 'ds-underline', 'ds-decoration-ui-stroke', 'hover:ds-text-typo-primary', 'hover:ds-decoration-ui-stroke-primary', 'ds-block', 'ds-mr-1', 'ds-cursor-pointer'])
#             while did_not_bat_names:
#                 player_name = did_not_bat_names.text.strip()
#                 player_data.append({'Player Name': player_name, 'Country': 'Did not bat'})
#                 did_not_bat_names = did_not_bat_names.find_next('a', class=['ds-text-tight-s', 'ds-font-medium', 'ds-text-typo', 'ds-underline', 'ds-decoration-ui-stroke', 'hover:ds-text-typo-primary', 'hover:ds-decoration-ui-stroke-primary', 'ds-block', 'ds-mr-1', 'ds-cursor-pointer'])
#
#         # Create a DataFrame from the player data
#         df = pd.DataFrame(player_data)
#
#         # Print the DataFrame
#         print(df)
#
#     else:
#         print("BATTING header not found in the HTML.")
#
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")
