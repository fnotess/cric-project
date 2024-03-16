import pandas as pd

# Load the CSV files into dataframes
output_sample_df = pd.read_csv('Output_sample_final.csv')
task42_df = pd.read_csv('Task42_removing_noresult.csv')
print(len(task42_df))

# Merge the dataframes based on player_id and scorecard columns
merged_df = pd.merge(task42_df, output_sample_df, on=['player_id', 'scorecard'], how='inner')

# Reorder the columns as per the specified order
result_df = merged_df[['player_name_x', 'player_id', 'url_x', 'team1_x', 'team2_x', 'winner_x', 'ground_x', 'margin_x',
                       'matchDate_x', 'matchDate2_x', 'scorecard', 'url2_x', 'player_team', 'Span', 'Matches', 'Runs',
                       'HS', 'Bat_Avg', '100s', 'Wkts', 'BBI', 'Bowl_Avg', '5fer', 'Catches', 'Stumping', 'Avg_Diff']]

# Rename the columns to remove suffixes added during merging
result_df.columns = result_df.columns.str.replace('_x', '')

# Save the resulting dataframe to a new CSV file
print(len(result_df))
result_df.to_csv('resulting_dataframe2.csv', index=False)
