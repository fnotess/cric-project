import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Read the CSV file containing the "url2" column
input_csv = 'task42_removing_noresult.csv'
output_csv = 'finaltask003.csv'
df = pd.read_csv(input_csv)
print('started')

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
df['Span'] = '0'
df['Matches'] = None
df['Runs'] = None
df['HS'] = None
df['Bat_Avg'] = None
df['100s'] = None
df['Wkts'] = None
df['BBI'] = None
df['Bowl_Avg'] = None
df['5fer'] = None
df['Catches'] = None
df['Stumping'] = None
df['Avg_Diff'] = None

# Iterate through the "url2" column and scrape values for each URL
x =0
for index, row in df.iterrows():

    print('inside')
    url2 = row['url2']
    values = scrape_values(url2)
    print(values)

    if values:
        # Assign values to the corresponding columns
        print('values')
        span = values[0]
        if '-' in span:
            df.at[index, 'Span'] = span
            df.at[index, 'Matches'] = values[1]
            df.at[index, 'Runs'] = values[2]
            df.at[index, 'HS'] = values[3]
            df.at[index, 'Bat_Avg'] = values[4]
            df.at[index, '100s'] = values[5]
            df.at[index, 'Wkts'] = values[6]
            df.at[index, 'BBI'] = values[7]
            df.at[index, 'Bowl_Avg'] = values[8]
            df.at[index, '5fer'] = values[9]
            df.at[index, 'Catches'] = values[10]
            df.at[index, 'Stumping'] = values[11]
            df.at[index, 'Avg_Diff'] = values[12]
        else:
            # If Span is '0', shift the values by 1 position
            df.at[index, 'Span'] = '0'
            df.at[index, 'Matches'] = values[0]
            df.at[index, 'Runs'] = values[1]
            df.at[index, 'HS'] = values[2]
            df.at[index, 'Bat_Avg'] = values[3]
            df.at[index, '100s'] = values[4]
            df.at[index, 'Wkts'] = values[5]
            df.at[index, 'BBI'] = values[6]
            df.at[index, 'Bowl_Avg'] = values[7]
            df.at[index, '5fer'] = values[8]
            df.at[index, 'Catches'] = values[9]
            df.at[index, 'Stumping'] = values[10]
            df.at[index, 'Avg_Diff'] = values[11]
        # Open the CSV file in append mode and write the player details

        with open(output_csv, 'a', newline='') as file:
            # writer = csv.writer(file)
            # print('append to the file')
            # print(x)
            # x = x+1
            # writer.writerow(df.iloc[index].values)

            writer = csv.writer(file)
            if index == 0:
                # Write headers only for the first row
                print('write headers')
                writer.writerow(df.columns)

            print('append to file: ' + str(index))
            print(x)
            x=x+1
            writer.writerow(df.iloc[index].values)

# Display the updated DataFrame
print(df)

print(f"Scraped values appended to {output_csv}")
