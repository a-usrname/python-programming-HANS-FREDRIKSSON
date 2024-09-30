import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#                                                              - Uppgift 1 -
#chatgpt-----------------------------------------------------------------------------------------------------------------------------------

# Read the original data file (Pichu and Pikachu data), skipping the first line
df = pd.read_csv('C:\Lärakod\ITHS\Python\PythonKursen\Lektioner\REPOS\python-programming-HANS-FREDRIKSSON\Labs\Labb2\datapoints.txt', skiprows=1, header=None)

# Assign column names: 'width', 'height', 'label'
df.columns = ['width', 'height', 'label']

# Create a test dataset (could be loaded from a file, here we define it manually)
test_data = {
    'width': [25, 24.2, 22, 20.5],  # Test data points' width
    'height': [32, 31.5, 34, 34]  # Test data points' height
}


test_df = pd.DataFrame(test_data)


#user input for another test point-----------------------------------------------------------
#obs lägg till try / exception sth så inte user kan mata in fel



while True:
    Try:
        user_width = int(input("mata in bredd mellan(): "))
        user_height = int(input("mata in höjd: "))


    Except:


    break



user_width = float(user_width)
user_height = float(user_height)

user_test_data = {
    'width': [user_width],  # User data points' width
    'height': [user_height]  # User Test data points' height
}

user_df = pd.DataFrame(user_test_data)
#-------------------------------------------------------------------------------------------

# ------------för att beräkna avstånd mellan testdata och originaldata, start-----------------------
# Function to calculate Euclidean distance----------
def euclidean_distance(row1, row2):
    return np.sqrt((row1['width'] - row2['width'])**2 + (row1['height'] - row2['height'])**2)

# Classify test data points based on nearest point in the original DataFrame
classifications = []
for i, test_point in test_df.iterrows():
    # Calculate distance to all points in the original dataset
    df['distance'] = df.apply(lambda row: euclidean_distance(row, test_point), axis=1)
    
    # Find the nearest point
    nearest_point = df.loc[df['distance'].idxmin()]
    
    # Classify as Pichu (0) or not Pichu (1)
    classifications.append(nearest_point['label'])

# Add classification results to the test_df
test_df['label'] = classifications

# ------------för att beräkna avstånd mellan testdata och originaldata, end-----------------------

# ------------för att beräkna avstånd mellan user och originaldata, start-----------------------
# Function to calculate Euclidean distance----------
def euclidean_distance(row1, row2):
    return np.sqrt((row1['width'] - row2['width'])**2 + (row1['height'] - row2['height'])**2)

# Classify test data points based on nearest point in the original DataFrame
classifications = []
for i, test_point in user_df.iterrows():
    # Calculate distance to all points in the original dataset
    df['distance'] = df.apply(lambda row: euclidean_distance(row, test_point), axis=1)
    
    # Find the nearest point
    nearest_point = df.loc[df['distance'].idxmin()]
    
    # Classify as Pichu (0) or not Pichu (1)
    classifications.append(nearest_point['label'])

# Add classification results to the test_df
user_df['label'] = classifications

# ------------för att beräkna avstånd mellan user data och originaldata, end-----------------------


# Scatter plot for original data (Pichu and Pikachu)
pichu = df[df['label'] == 0]
pikachu = df[df['label'] == 1]

plt.scatter(pichu['width'], pichu['height'], color='blue', label='Pichu (label 0)')
plt.scatter(pikachu['width'], pikachu['height'], color='yellow', label='Pikachu (label 1)')

# Scatter plot for test data points (classified as Pichu or Pikachu)
test_pichu = test_df[test_df['label'] == 0]
test_not_pichu = test_df[test_df['label'] == 1]

plt.scatter(test_pichu['width'], test_pichu['height'], color='green', label='Test Pichu')
plt.scatter(test_not_pichu['width'], test_not_pichu['height'], color='red', label='Test Pikachu')

# Scatter plot for USER test data points (classified as Pichu or Pikachu)-------------------------
test_pichu = user_df[user_df['label'] == 0]
test_not_pichu = user_df[user_df['label'] == 1]

plt.scatter(test_pichu['width'], test_pichu['height'], color='black', label='User Test Pichu')
plt.scatter(test_not_pichu['width'], test_not_pichu['height'], color='brown', label='User Test Pikachu')

#--------------------------------------------------------------------------------------------

# Adding labels and title
plt.xlabel('Width')
plt.ylabel('Height')
plt.title('Scatter plot of Pichu, Pikachu, and Test Points')
plt.legend()

# Display the plot
plt.show()

# Print test data classification
print("Test Data Classification Results:")
print(test_df)

#chatgpt-----------------------------------------------------------------------------------------------------------------------------------





#                                                              - Uppgift 2 -
