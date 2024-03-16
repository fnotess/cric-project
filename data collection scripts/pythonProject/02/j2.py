import pandas as pd

# Load the CSV files into pandas dataframes
df1 = pd.read_csv('task42_removing_noresult.csv')
df2 = pd.read_csv('output_sample_final.csv')

print(len(df1))
print(len(df2))

# Identify common columns
common_columns = set(df1.columns) & set(df2.columns)
print(common_columns)

# Identify extra columns in df2
extra_columns_in_df2 = set(df2.columns) - set(df1.columns)
print(extra_columns_in_df2)

# Include additional column from df1 in common columns
common_columns.add('player_team')
print(common_columns)

# Create a list to store DataFrames
merged_dfs = []

# Iterate through the rows of the smaller dataframe (df1)
for index, row in df1.iterrows():
    # Find matching record in df2 based on player_id and scorecard columns
    print(index)
    matching_row = df2[(df2['player_id'] == row['player_id']) & (df2['scorecard'] == row['scorecard'])]

    if not matching_row.empty:
        # Merge the data from both dataframes
        merged_row = pd.concat([row, matching_row.iloc[0]])

        # Append the merged row to the list of DataFrames
        merged_dfs.append(merged_row)

# Combine all DataFrames in the list into a single DataFrame
merged_df = pd.concat(merged_dfs, ignore_index=True)

# # Add extra columns from df2 to the merged dataframe
# merged_df = pd.concat([merged_df, df2[extra_columns_in_df2]], axis=1)

# Add extra columns from df2 to the merged dataframe
merged_df = pd.concat([merged_df, df2[list(extra_columns_in_df2)]], axis=1)


# Save the merged dataframe to a new CSV file
merged_df.to_csv('merged_output.csv', index=False)
