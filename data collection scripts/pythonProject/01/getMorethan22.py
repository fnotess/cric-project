import pandas as pd

# Read the file into a DataFrame
file_path = 'task42_removing_noresult.csv'  # Replace with the actual path to your file
df = pd.read_csv(file_path)

# Assuming 'scorecard' is the column name with the numbers
scorecard_column = 'scorecard'

# Count the occurrences of each number in the 'scorecard' column
scorecard_counts = df[scorecard_column].value_counts()
print(scorecard_counts)





# Filter numbers that occur more or less than 22 times
selected_numbers = scorecard_counts[(scorecard_counts > 22) | (scorecard_counts < 22)].index.tolist()

# Filter the DataFrame based on the selected numbers
filtered_df = df[df[scorecard_column].isin(selected_numbers)]

# Display the resulting DataFrame
print(filtered_df)
print(len(filtered_df))

print(filtered_df[scorecard_column])

# Display the distinct values in the 'scorecard' column after filtering
distinct_values_after_filtering = filtered_df[scorecard_column].unique()
print("Distinct values in 'scorecard' column after filtering:")
print(distinct_values_after_filtering)
print(len(distinct_values_after_filtering))


# Assuming 'winner' is the column name
winner_column = 'winner'

# Filter records where 'winner' is equal to 'No Result'
no_result_records = df[df[winner_column] == 'no result']

# Display the number of records where 'winner' is 'No Result'
num_no_result_records = len(no_result_records)
print(f"Number of records where 'winner' is 'No Result': {num_no_result_records}")


# Remove rows where 'winner' is equal to 'No Result'
df_filtered = df[df[winner_column] != 'no result']

# Display the resulting DataFrame
print("DataFrame after removing rows where 'winner' is 'No Result':")
print(df_filtered)
print(len(df_filtered))

# Save the filtered DataFrame to a new CSV file
output_csv_path1 = 'task42_removing_noresult.csv'

print(len(df))
print(len(df_filtered))

# Remove rows where 'scorecard' is equal to 4339
df_filtered2 = df_filtered[df_filtered[scorecard_column] != 4339]

# Display the resulting DataFrame
print("DataFrame after removing rows where 'scorecard' is 4339:")
print(df_filtered2)

# Save the filtered DataFrame to a new CSV file
#df_filtered2.to_csv(output_csv_path1, index=False)
print(f"Filtered data saved to {output_csv_path1}")

# df_filtered.to_csv(output_csv_path1, index=False)

print(len(df_filtered2)/22)




