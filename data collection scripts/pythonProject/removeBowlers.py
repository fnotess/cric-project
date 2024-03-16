import pandas as pd

# Replace 'your_input_csv_file.csv' with the actual file name containing the DataFrame
input_csv = 'output_with_url2.csv'

# Read the DataFrame from the CSV file
df = pd.read_csv(input_csv)

# Remove rows where 'player_name' column contains 'View full profile of'
df = df[~df['player_name'].fillna('').str.contains('View full profile of')]

# Remove duplicates based on all columns except 'player_name'
df = df[~df.duplicated(subset=df.columns.difference(['player_name']))]

# Display the remaining rows
print(df)

# Replace 'your_output_csv_file.csv' with the desired file name for the final CSV file
output_csv = 'no_duplicates_csv_file2.csv'

# Write the remaining rows to the final CSV file
df.to_csv(output_csv, index=False)

print(f"Remaining rows written to {output_csv}")
