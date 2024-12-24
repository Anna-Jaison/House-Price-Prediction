# House Price Prediction

This project uses a **linear regression model** to predict house prices based on features such as square footage, number of bedrooms, and number of bathrooms. 

The dataset used for training and testing is sourced from the [Kaggle competition: House Prices - Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data).

---

## Features
The model uses the following features for predicting house prices:
- **Square Footage**: Total area of the house in square feet.
- **Number of Bedrooms**: Total number of bedrooms in the house.
- **Number of Bathrooms**: Total number of bathrooms in the house.

---

## Project Directory Structure
House-Price-Prediction/ │
├── house_prices/ # Dataset folder │ 
   ├── train.csv # Training dataset │
   └── test.csv # Testing dataset
├── models/ # Folder for saved model │ 
   └── house_price_model.pkl # Trained model file
├── src.py # Python script for training and evaluation 
---

## Installation Instructions

### Prerequisites
- Python 3.7 or above
- Required libraries: `pandas`, `numpy`, `scikit-learn`

### Steps to Clone and Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/Anna-Jaison/House-Price-Prediction.git
2. Navigate to the project directory:
   ```bash
   cd House-Price-Prediction
3. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
4. Run the Python script to train the model:
   ```bash
    python src.py

### Output
The trained model is saved as house_price_model.pkl in the models/ folder.
Evaluation metrics such as Mean Squared Error (MSE) and R² (R-squared) are displayed in the terminal after the script runs.

### Dataset
The dataset includes:

- train.csv: Used for training the model.
- test.csv: Used for testing and evaluation.
- Source: Kaggle Dataset



