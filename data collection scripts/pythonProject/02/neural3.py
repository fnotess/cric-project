import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import tensorflow as tf
from tensorflow.keras import layers, models

# Load data from CSV file
data = pd.read_csv('cric_csv_with_winner3.csv')

# Replace '-' with 0 in the specified columns
columns_to_replace = ['Matches', 'Runs', 'HS_without_asterisk', 'Bat_Avg', '100s', 'Wkts', 'Bowl_Avg', '5fer', 'Catches', 'Stumping', 'Avg_Diff']
data[columns_to_replace] = data[columns_to_replace].replace('-', 0)

# Replace '*' with blank in the 'HS' column
# data['HS'] = data['HS'].str.replace('*', '')
#
# # Convert 'HS' column to numeric, handling other non-numeric values
# data['HS'] = pd.to_numeric(data['HS'], errors='coerce').fillna(0).astype(int)

# print(data['HS'].unique())

# Remove the 'HS' column from the DataFrame
# data.drop('HS', axis=1, inplace=True)


# Encode country names (output labels)
label_encoder = LabelEncoder()
data['Winner'] = label_encoder.fit_transform(data['Winner'])

# Replace '*' with blank in the entire DataFrame
data = data.replace('*', '')

# Create a list to store match-wise features and labels
match_features = []
match_labels = []

# Group data by match ID
grouped_data = data.groupby('scorecard')

for group_name, group_data in grouped_data:
    # Select the first 11 records for team 1 and the next 11 records for team 2
    team1_data = group_data.iloc[:11]
    team2_data = group_data.iloc[11:22]

    # Extract relevant columns for each player
    team1_features = team1_data[['Matches', 'Runs', 'HS_without_asterisk', 'Bat_Avg', '100s', 'Wkts', 'Bowl_Avg', '5fer', 'Catches', 'Stumping', 'Avg_Diff']].values.flatten()
    team2_features = team2_data[['Matches', 'Runs', 'HS_without_asterisk', 'Bat_Avg', '100s', 'Wkts', 'Bowl_Avg', '5fer', 'Catches', 'Stumping', 'Avg_Diff']].values.flatten()

    # Combine the features of both teams
    match_features.append(pd.concat([pd.Series(team1_features), pd.Series(team2_features)], axis=0, ignore_index=True))
    match_labels.append(group_data['Winner'].iloc[0])
    # print(group_data['Winner'])

print(match_features)
# Convert the list of features and labels to DataFrame
X = pd.DataFrame(match_features)

# Reset the index to ensure uniqueness
# X.reset_index(drop=True, inplace=True)

y = pd.Series(match_labels)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train)
X_train = X_train.replace('*', '')


# Find the row and column where '*' occurs
row, col = (X_train == '*').values.any(axis=1), (X_train == '*').values.any(axis=0)

# Get the indices of the row and column where '*' occurs
row_indices, col_indices = row.argmax(), col.argmax()

# Print the row and column where '*' occurs
print(f"Row index 1: {row_indices}, Column index 1: {col_indices}")

# Standardize the input features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create the model
model = models.Sequential()

# Input layer
model.add(layers.InputLayer(input_shape=(X_train.shape[1],)))

# Hidden layers
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(32, activation='relu'))

# Output layer with softmax activation for multi-class classification
model.add(layers.Dense(len(label_encoder.classes_), activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
print("Training started...")
history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {test_acc}')

# Print training history
print("Training History:")
print(history.history)
