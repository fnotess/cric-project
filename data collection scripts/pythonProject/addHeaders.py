import pandas as pd

# Assuming your CSV file without headers is named 'input.csv'
input_csv = 'output_player_details_final.csv'
output_csv = 'output_final_final.csv'

# Specify the column names
columns = ['player_name', 'player_id', 'url', 'team1', 'team2', 'winner', 'ground', 'margin', 'matchDate', 'matchDate2', 'scorecard']

# Read the CSV file without headers
df = pd.read_csv(input_csv, names=columns)

# Write the DataFrame with headers to another CSV file
df.to_csv(output_csv, index=False)

# Display the updated DataFrame
print(df.head())
