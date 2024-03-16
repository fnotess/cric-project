import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

# Read the CSV file containing the "url2" column
input_csv = 'no_dupes2.csv'
output_csv = 'output_sample.csv'
df = pd.read_csv(input_csv)

# Function to scrape values from the specified table section
def scrape_values(url2):
    response = requests.get(url2)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <tbody> sections
        tbody_sections = soup.find_all('tbody')

        # Check if there is a second <tbody> section
        if len(tbody_sections) > 1:
            # Select the second <tbody> section
            tbody = tbody_sections[1]

            # Find the <td> section with class "left" and content "filtered" inside the selected <tbody>
            filtered_td = tbody.find('td', class_='left', string='filtered')

            # Extract values from the siblings of the found <td>
            if filtered_td:
                values = [td.get_text(strip=True) for td in filtered_td.find_next_siblings('td')][:13]
                return values

    return None

# Create new columns for the extracted values
new_columns = ['Span', 'Matches', 'Runs', 'HS', 'Bat_Avg', '100s', 'Wkts', 'BBI', 'Bowl_Avg', '5fer', 'Catches', 'Stumping', 'Avg_Diff']

# Read the original CSV file
df = pd.read_csv(input_csv)

# Append new columns to the DataFrame
for col in new_columns:
    df[col] = None

# Iterate through the "url2" column and append scraped values to the DataFrame and CSV file
with open(output_csv, 'a', newline='') as file:
    writer = csv.writer(file)

    for index, row in df.iterrows():
        url2 = row['url2']
        values = scrape_values(url2)

        if values:
            # Combine the original values with the scraped values
            combined_values = row.tolist() + values

            # Append the combined values to the CSV file
            writer.writerow(combined_values)

            # Update the DataFrame with the combined values
            df.loc[index, new_columns] = values

# Display the updated DataFrame
print(df)

print(f"Scraped values appended to {output_csv}")


