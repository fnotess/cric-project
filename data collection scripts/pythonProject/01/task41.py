import pandas as pd

input_csv = 'task261.csv'

df = pd.read_csv(input_csv)

# Convert the "matchDate" column to the desired format
#df['matchDate'] = pd.to_datetime(df['matchDate'], format='%b %d, %Y').dt.strftime('%d+%b+%Y')
# Convert the "matchDate" column to the desired format
df['matchDate'] = pd.to_datetime(df['matchDate'], errors='coerce', infer_datetime_format=True)
df['matchDate'] = df['matchDate'].dt.strftime('%d+%b+%Y')

# Function to create the "url2" column based on "matchDate" and "player_id"
def create_url(row):
    base_url = 'https://stats.espncricinfo.com/ci/engine/player/'
    player_id = row['player_id']
    match_date = row['matchDate']
    url2 = f'{base_url}{player_id}.html?class=2;filter=advanced;orderby=default;spanmax1={match_date};spanval1=span;template=results;type=allround'
    print(url2)
    return url2

# Apply the function to create the "url2" column
df['url2'] = df.apply(create_url, axis=1)

# Display the updated DataFrame
print(df)

# Remove duplicates based on all fields
df = df.drop_duplicates()

# Write the final DataFrame to a CSV file
output_csv = 'task41.csv'
df.to_csv(output_csv, index=False)
print(f"DataFrame written to {output_csv}")
