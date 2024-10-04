import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# got code from chatgpt, then modified it with other variable names and etc
# Read the original data file (Pichu and Pikachu data), skipping the first line
# and assigned column names
df = pd.read_csv('datapoints.txt', skiprows=1, header=None)
df.columns = ['width', 'height', 'label']

# user input for test point with while loop with try/except to prevent wrong input from user
while True:          
    try:
        user_width = float(input("mata in bredd(mellan 15.5-28.5): "))
        user_height = float(input("mata in höjd(mellan 27.5-38.5): "))
        
        if  (user_width <= 15.5 or user_width >= 28.5):
            print(f"båda måste vara innanför intervallen, testa igen")
            continue    #go to next iteration of the loop

        if (user_height <= 27.5 or user_height >= 38.5):
            print(f"båda måste vara innanför intervallen, testa igen")
            continue 
        break
    except ValueError:
        # Om user annat än float
        print("bara siffror, tack")

# test data points from user input
test_data_from_user_input = {
    'width': [user_width],  # User data points' width
    'height': [user_height]  # User Test data points' height
}

# create data frame from user input
user_input_df = pd.DataFrame(test_data_from_user_input)

# copy user data frame to KNN data frame to be used for KNN test  
test_df_knn = user_input_df

# Function to calculate Euclidean distance
# (between original data points and user test data point)
# row1 first data point, row 2 second data point
def euclidean_distance(row1, row2):
    return np.sqrt((row1['width'] - row2['width'])**2 + (row1['height'] - row2['height'])**2)

# --------------------------------- Task 1 ---------------------
# Classify user test data points based on nearest point in the original DataFrame
classifications = []
for i, test_point in user_input_df.iterrows():
    # Calculate distance to all points in the original dataset
    df['distance'] = df.apply(lambda row: euclidean_distance(row, test_point), axis=1)
    
    # Find the nearest point
    nearest_point = df.loc[df['distance'].idxmin()]
    
    # Classify as Pichu (0) or not Pichu (1)
    classifications.append(nearest_point['label'])

# Add classification results to the user input data frame
user_input_df['label'] = classifications
#----------------------------------------------------------------

# --------------------------------- Task 2 ---------------------
# Use KNN to get better classification (according to chatgpt), 10 data points instead of 1, based on majority vote
# K-Nearest Neighbors function (KNN)      (function from chatgpt did not modify)    
def knn_classify(test_point, k):
    # Calculate distances from test_point to all points in df
    df['distance'] = df.apply(lambda row:euclidean_distance(row, test_point), axis=1)

    #Sort by distance and take the k nearest neighbors
    nearest_neighbors = df.nsmallest(k, 'distance')

    #Get the labels of the nearest neighbors
    nearest_labels = nearest_neighbors['label']

    #Count the occurrences of each label and return the most common one
    label_count = Counter(nearest_labels)
    majority_label = label_count.most_common(1)[0][0]

    return majority_label

# KNN choose k value (for how many neighbors to compare with)
k = 10

#Classify each point based on KNN
classifications =[]
for i, test_point in test_df_knn.iterrows():
    #Classify using KNN
    classification = knn_classify(test_point, k)

    #Print the K nearest neighbor for debugging... 
    #print(f"Test point {i} ({test_point['width']}), {test_point['height']}) classified as {classification}")

    #Append the classification result
    classifications.append(classification)

# KNN Add classification result
test_df_knn['label'] = classifications
#----------------------------------------------------------------

# Setting data for the Scatter plot and displaying the plot
# plot data for ORIGINAL DATA (chatgpt) 
pichu = df[df['label'] == 0]
pikachu = df[df['label'] == 1]

plt.scatter(pichu['width'], pichu['height'], color='blue', label='Pichu (label 0)')
plt.scatter(pikachu['width'], pikachu['height'], color='yellow', label='Pikachu(Not Pichu) (label 1)')

# Scatter plot for USER test data points (classified as Test Pichu or Test Not Pichu)
test_pichu = user_input_df[user_input_df['label'] == 0]
test_not_pichu = user_input_df[user_input_df['label'] == 1]

plt.scatter(test_pichu['width'], test_pichu['height'], color='black', label='Test Pichu (label 0)')
plt.scatter(test_not_pichu['width'], test_not_pichu['height'], color='red', label='Test Not Pichu (label 1)')

# KNN Scatter plot data for TEST DATA of User input (classified as KNN Test Pichu or KNN Test Not Pichu)
test_pichu = test_df_knn[user_input_df['label'] == 0]
test_not_pichu = test_df_knn[user_input_df['label'] == 1]

plt.scatter(test_pichu['width'], test_pichu['height'], color='red', marker='x', label='KNN Test Pichu (label 0)')
plt.scatter(test_not_pichu['width'], test_not_pichu['height'], color='black', marker='x', label='KNN Test Not Pichu (label 1)')

# Adding labels and title to the Scatter plot
plt.xlabel('Width')
plt.ylabel('Height')
plt.title(f'Scatter plot of Pichu, Pikachu and \n two classification methods of the User Test Point')
plt.legend()

# Print test data classification
print("Test Data Classification Results:")
print(user_input_df)
print("")
print("KNN Test Data Classification Results:")
print(test_df_knn)

# Display the plot
plt.show()

