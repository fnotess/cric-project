import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import tensorflow as tf
from tensorflow.keras import layers, models

# Step 1: Data Preprocessing

# Load data from CSV file
data = pd.read_csv('your_data.csv')

# Encode country names (output labels)
label_encoder = LabelEncoder()
data['winner'] = label_encoder.fit_transform(data['winner'])

# Separate features (X) and labels (y)
X = data.drop(['winner'], axis=1)
y = data['winner']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the input features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 2: Model Architecture

# Create the model
model = models.Sequential()

# Input layer
model.add(layers.InputLayer(input_shape=(X_train.shape[1],)))

# Hidden layers (you can experiment with the number of layers and neurons)
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(32, activation='relu'))

# Output layer with softmax activation for multi-class classification
model.add(layers.Dense(len(label_encoder.classes_), activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Step 3: Model Training

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Step 4: Model Evaluation

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {test_acc}')

# Step 5: Make Predictions

# Assuming you have a new_data DataFrame with the same structure as your training data
new_data = pd.read_csv('your_new_data.csv')
new_data_scaled = scaler.transform(new_data)
predictions = model.predict(new_data_scaled)

# Decode the predicted labels back to country names
predicted_countries = label_encoder.inverse_transform(predictions.argmax(axis=1))
print(f'Predicted Winners: {predicted_countries}')
