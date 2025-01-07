# Importing necessary libraries
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib 
import os 

# Section 1: Loading and Exploring the Dataset

# Loading the dataset from 'data.csv' into a pandas DataFrame
data = pd.read_csv('data.csv', encoding='unicode_escape')

# Displaying the first few rows of the dataset for initial exploration
print("First few rows of the dataset:")
print(data.head())

# Section 2: Data Visualization

# Data Visualization - Relational plot for Maintenance vs Engine Speed
print("Relational plot for Maintenance vs Engine Speed:")
sns.relplot(x='Maintenance', y='Engine Speed (RPM)', data=data)
plt.title('Maintenance vs Engine Speed')
plt.show()

# Data Visualization - Relational plot for Engine Speed vs Generator Avg Frequency
print("Relational plot for Engine Speed vs Generator Avg Frequency:")
sns.relplot(x='Engine Speed (RPM)', y='Generator Avg Frequency (Hz)', data=data)
plt.title('Engine Speed vs Generator Avg Frequency')
plt.show()

# Data Visualization - Relational plot for Engine Speed vs Battery Voltage
print("Relational plot for Engine Speed vs Battery Voltage:")
sns.relplot(x='Engine Speed (RPM)', y='Battery Voltage (V)', data=data)
plt.title('Engine Speed vs Battery Voltage')
plt.show()

# Section 3: Data Preparation

# Defining features and target variable
features = ['Battery Voltage (V)', 'Coolant Temperature (°C)', 'Engine Speed (RPM)', 'Generator Avg Frequency (Hz)']
target = 'Maintenance'

# Splitting data into training and testing sets
X = data[features]
y = data[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Section 4: Model Initialization, Training, and Prediction

# Initializing a Random Forest Classifier
clf = RandomForestClassifier(random_state=42)

# Training the classifier on the training data
clf.fit(X_train, y_train)

# Save the trained model to a file in the 'models' folder

model_directory = 'models'
model_filename = 'random_forest_model.joblib'
model_path = os.path.join(model_directory, model_filename)

# Check if the 'models' directory exists, create it if not
if not os.path.exists(model_directory):
    os.makedirs(model_directory)

# Save the model
joblib.dump(clf, model_path)
print(f"Model saved to {model_path}")

# Making predictions on the test data
y_pred = clf.predict(X_test)

# Section 5: Model Evaluation

# Calculating and printing Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy:.2f}')

# Printing Classification Report
report = classification_report(y_test, y_pred)
print('Classification Report:\n', report)

# Save the trained model to a file in the 'models' folder
model_filename = 'models/random_forest_model.joblib'
joblib.dump(clf, model_filename)
print(f"Model saved to {model_filename}")
