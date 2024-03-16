# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

def scrape_match_results(url):
    response = requests.get(url)

    data = []
    headers = ["Team 1", "Team 2", "Winner", "Margin", "Ground", "Match Date", "Scorecard", "Link"]

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Print the page's HTML content to check if the table is present
        print(soup.prettify())

        tbody = soup.find('tbody')

        # Find all table rows (tr) within the table body
        rows = tbody.find_all('tr')

        # Iterate through each row to extract the required data
        for row in rows:
            # Find all table data (td) within the row
            cells = row.find_all('td')
            if len(cells) == 7:  # Ensure that the row contains the expected number of cells
                team1 = cells[0].text.strip()
                team2 = cells[1].text.strip()
                winner = cells[2].text.strip()
                margin = cells[3].text.strip()
                ground = cells[4].text.strip()
                match_date = cells[5].text.strip()
                scorecard = cells[6].text.strip().replace("ODI # ", "")

                # Find the link within the last cell (scorecard link)
                scorecard_link = cells[6].find('a')['href']
                scorecard_link = "https://www.espncricinfo.com" + scorecard_link

                # Append the extracted data to the list
                data.append([team1, team2, winner, margin, ground, match_date, scorecard, scorecard_link])

            # Create a DataFrame from the data list
        df = pd.DataFrame(data, columns=["Team 1", "Team 2", "Winner", "Margin", "Ground", "Match Date","Scorecard","Scorecard Link"])

        print(df)
        return df
        # Write the data to a CSV file
        # output_file = "odi_match_results_1999.csv"
        # with open(output_file, 'w', newline='') as csvfile:
        #     csv_writer = csv.writer(csvfile)
        #
        #     # Write the header row
        #     csv_writer.writerow(headers)
        #
        #     # Write the data rows
        #     csv_writer.writerows(data)
        #
        # print("Data has been scraped and saved to", output_file)

        # Find the table containing match results
        # table = soup.find("table", class_="engineTable")
        #
        # # print(table)
        #
        #
        #
        # # Initialize lists to store data
        # match_dates = []
        # teams = []
        # results = []
        # match_links = []
        #
        # # Extract data from each row in the table
        # for row in table.find_all("tr")[1:]:  # Skip the table header row
        #     cells = row.find_all("td")
        #     match_date = cells[0].text.strip()
        #     team = cells[1].text.strip()
        #     result = cells[2].text.strip()
        #     match_link = cells[2].find("a")["href"] if cells[2].find("a") else ""
        #
        #     match_dates.append(match_date)
        #     teams.append(team)
        #     results.append(result)
        #     match_links.append(match_link)
        #
        # # Create a DataFrame
        # df = pd.DataFrame({
        #     "Match Date": match_dates,
        #     "Team": teams,
        #     "Result": results,
        #     "Match Link": match_links
        # })
        #
        # return df

    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return None


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    #
    # url = "https://www.espncricinfo.com/records/year/team-match-results/1999-1999/one-day-internationals-2"
    # df = scrape_match_results(url)
    #
    # if df is not None:
    #     # Save DataFrame to CSV
    #     df.to_csv("odi_match_results_1999.csv", index=False)
    #     print("Data scraped and saved to odi_match_results_1999.csv")

    # Initialize an empty DataFrame to store the combined results
    combined_df = pd.DataFrame()

    # Scrape match results for years 1980 to 2022
    for year in range(1997, 2022):
        url = f"https://www.espncricinfo.com/records/year/team-match-results/{year}-{year}/one-day-internationals-2"
        df = scrape_match_results(url)

        if df is not None:
            # Append the current year's DataFrame to the combined DataFrame
            combined_df = pd.concat([combined_df, df], ignore_index=True)

    # Save the combined DataFrame to a CSV file
    combined_df.to_csv("odi_match_results_1997_to_2022.csv", index=False)
    print("Data scraped and saved to odi_match_results_1997_to_2022.csv")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
