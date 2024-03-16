import pandas as pd

# Read the CSV file
data = pd.read_csv('cric_csv_with_winner.csv')

# Replace '*' with empty string in the entire DataFrame
data.replace('*', '', inplace=True)

# Write the modified DataFrame to another CSV file
data.to_csv('cric_csv_with_winner2.csv', index=False)

print("CSV file with '*' replaced has been saved as 'output_file.csv'.")
