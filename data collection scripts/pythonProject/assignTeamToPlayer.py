import pandas as pd

# Read the existing CSV file with 90k records
input_file_path = 'output_sample_final.csv'
df = pd.read_csv(input_file_path)

# Function to assign player_team based on the condition
# Function to assign player_team based on the condition
def assign_team(player_number):
    if player_number <= 11:
        return 'Team1'
    else:
        return 'Team2'

# Apply the function to create the 'player_team' column
df['player_team'] = (df.groupby('scorecard').cumcount() % 22) + 1
df['player_team'] = df.apply(lambda row: row['team1'] if row['player_team'] <= 11 else row['team2'], axis=1)

# Save the modified dataframe to a new CSV file
output_file_path = 'output_sample_final62.csv'
df.to_csv(output_file_path, index=False)

print("CSV file with player_team column created successfully.")
