import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


#                                                              - Uppgift 2 -
# use KNN to get better classification, 10 data points instead of 1, base on majority vote
#chatgpt-----------------------------------------------------------------------------------------------------------------------------------

# Read the original data file (Pichu and Pikachu data), skipping the first line
df = pd.read_csv('C:\Lärakod\ITHS\Python\PythonKursen\Lektioner\REPOS\python-programming-HANS-FREDRIKSSON\Labs\Labb2\datapoints.txt', skiprows=1, header=None)

# Assign column names to the data frame: 'width', 'height', 'label'
df.columns = ['width', 'height', 'label']

# Create a test dataset (could be loaded from a file, here we define it manually)
test_data = {
    'width': [25, 24.2, 22, 20.5],  # Test data points' width
    'height': [32, 31.5, 34, 34]  # Test data points' height
}

test_df = pd.DataFrame(test_data)



# ------------för att beräkna avstånd mellan testdata och originaldata, start-----------------------
# Function to calculate Euclidean distance----------
def euclidean_distance(row1, row2):
    return np.sqrt((row1['width'] - row2['width'])**2 + (row1['height'] - row2['height'])**2)

# K-Nearest Neighbors function                     (obs! this one for test point only not user input data points, need to fix)
def knn_classify(test_point, k):
    # Calculate distances from test_point to all points in df
    df['distance'] = df.apply(lambda row:euclidean_distance(row, test_point), axis=1)

    #Sort by distance and take the k nearest neighbors
    nearest_neighbors = df.nsmallest(k, 'distance')

    #Get the labels of the nearest neighbors
    nearest_labels = nearest_neighbors['label']

    #COunt the occurrences of each label and return the most common one
    label_count = Counter(nearest_labels)
    majority_label = label_count.most_common(1)[0][0]

    return majority_label
#---------------------------------------------------------------------------------------------------

# choose k value (for how many neighbors to compare with)
k = 10

#Classify each point based on KNN---------------------
classifications =[]
for i, test_point in test_df.iterrows():
    #Classify using KNN
    classification = knn_classify(test_point, k)

    #Print the K nearest neighbor for debugging...
    print(f"Test point {i} ({test_point['width']}), {test_point['height']}) classified as {classification}")

    #Append the classification result
    classifications.append(classification)
#----------------------------------------------------

#Add classification result
test_df['label'] = classifications

#Scatter plot for ORIGINAL DATA---------------------
pichu = df[df['label'] == 0]
pikachu = df[df['label'] == 1]

plt.scatter(pichu['width'], pichu['height'], color='blue', label='Pichu (label 0)')
plt.scatter(pikachu['width'], pikachu['height'], color='yellow', label='Pikachu (label 1)')
#----------------------------------------------------

#Scatter plot for TEST DATA---------------------
test_pichu = test_df[test_df['label'] == 0]
test_not_pichu = test_df[test_df['label'] == 1]

plt.scatter(test_pichu['width'], test_pichu['height'], color='green', marker='x', label='Test_Pichu (label 0)')
plt.scatter(test_not_pichu['width'], test_not_pichu['height'], color='red', marker='x', label='Test_Not_Pichu (label 1)')
#----------------------------------------------------

# MAIMEE SCATTER PLOT FOR USER INPUT-------




#-------------------------------------------


# Adding labels and title
plt.xlabel('Width')
plt.ylabel('Height')
plt.title(f'Scatter plot of Pichu, Pikachu, and Test Points (k={k})')
plt.legend()

# Display the plot
plt.show()

# Print test data classification
print("Test Data Classification Results:")
print(test_df)

#chatgpt-----------------------------------------------------------------------------------------------------------------------------------









