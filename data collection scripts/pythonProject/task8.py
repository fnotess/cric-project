from datetime import time

import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.espncricinfo.com/series/world-cup-league-2-2019-2023-1196667/nepal-vs-scotland-120th-match-1341980/full-scorecard'
response = requests.get(url)
print(response)

# time.sleep(5)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)

    cricketers_data = []

    # Find all tables with the specified class
    tables = soup.find_all('table', class_='ds-w-full ds-table ds-table-xs ds-table-auto ci-scorecard-table')
    print(tables)

    for table in tables:
        # Find all links within the table with the specified href pattern
        cricketer_links = table.find_all('a', href=lambda href: href and '/cricketers/' in href)

        for link in cricketer_links:
            cricketer_url = link.get('href')
            cricketer_title = link.get('title')

            cricketers_data.append({'url': cricketer_url, 'title': cricketer_title})

    # Write data to CSV file
    csv_file_path = 'cricketers_data_task8.csv'
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['url', 'title']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write data rows
        for cricketer in cricketers_data:
            writer.writerow(cricketer)

    print(f'Successfully scraped and saved data to {csv_file_path}')

else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
