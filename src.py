# Import Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

# Define the Dataset Path
folder_path = 'C:/Users/JOSEP/Desktop/House-Price-Prediction/house_prices'
file_name = 'train.csv'  # Adjust this if the file has a different name
file_path = os.path.join(folder_path, file_name)

# Check if the File Exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"File not found: {file_path}")

# Load Dataset
data = pd.read_csv(file_path)
print("Dataset loaded successfully!")
print(data.head())

# Feature Selection (Modify as per your dataset)
features = ['GrLivArea', 'BedroomAbvGr', 'FullBath']  # Example features
target = 'SalePrice'

# Check if the required columns exist
for column in features + [target]:
    if column not in data.columns:
        raise KeyError(f"Missing column in dataset: {column}")

X = data[features]
y = data[target]

# Handle Missing Values (if any)
X = X.fillna(X.mean())
y = y.fillna(y.mean())

# Split the Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Make Predictions
y_pred = model.predict(X_test)

# Evaluate the Model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R² Score: {r2}")

# Save the Model
model_folder = 'C:/Users/JOSEP/Desktop/House-Price-Prediction/models'
os.makedirs(model_folder, exist_ok=True)
model_path = os.path.join(model_folder, 'house_price_model.pkl')
joblib.dump(model, model_path)
print(f"Model saved at: {model_path}")

