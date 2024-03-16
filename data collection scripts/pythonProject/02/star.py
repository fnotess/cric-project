import pandas as pd

# Read the CSV file
data = pd.read_csv('cric_csv_with_winner.csv')

print(data['HS'])

# Replace '*' with empty string in the 'HS' column (apply directly to `data`)
data['HS'] = data['HS'].str.replace('*', '')  # Remove '*' from any position

# Print the modified column to verify
print(data['HS'])

data['HS_without_asterisk'] = data['HS'].astype(str)

data.drop('HS', axis=1, inplace=True)

print(data['Runs'])

data['Runs'] = data['Runs'].str.replace('*', '')  # Remove '*' from any position

print(data['Runs'])

# data['HS'] = data['HS'].astype(str)

# Save the modified DataFrame to the correct file
data.to_csv('cric_csv_with_winner3.csv', index=False)

print("CSV file with '*' replaced in the 'HS' column has been saved as 'cric_csv_with_winner3.csv'.")
