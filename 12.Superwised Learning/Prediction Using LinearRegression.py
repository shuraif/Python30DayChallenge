from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings

# Suppress the specific warning
warnings.filterwarnings("ignore", message="X does not have valid feature names, but LinearRegression was fitted with feature names")


# Sample dataset
data = pd.DataFrame({
    'Experience':       [2, 3, 5, 7, 4, 8, 6, 1, 9, 2],
    'TechnologySkills': [7, 6, 8, 5, 9, 4, 7, 3, 8, 6],
    'Salary': [55000, 60000, 75000, 85000, 62000, 92000, 81000, 48000, 98000, 56000]
})

# Display the sample dataset
print(data)

# Split the data into features (X) and target (y)
X = data[['Experience', 'TechnologySkills']]
y = data['Salary']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Linear Regression model
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model's performance
from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)


X_new = np.array([[2,6]])

# Make predictions
predictions = model.predict(X_new)
print((predictions))