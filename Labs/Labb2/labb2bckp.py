import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

#lägg uppg1+2 i samma, kör två olika scatterplots på slutet, upprepa ej kod - gör funktioner istället
#ta inte med sample punkterna




#chatgpt-----------------------------------------------------------------------------------------------------------------------------------

# Read the original data file (Pichu and Pikachu data), skipping the first line
df = pd.read_csv('C:\Lärakod\ITHS\Python\PythonKursen\Lektioner\REPOS\python-programming-HANS-FREDRIKSSON\Labs\Labb2\datapoints.txt', skiprows=1, header=None)

# Assign column names to the data frame: 'width', 'height', 'label'
df.columns = ['width', 'height', 'label']

#user input for another test point-----------------------------------------------------------
# while loop for handling input other than float
while True:    
            
    try:
        user_width = float(input("mata in bredd(mellan 15.5-28.5): "))
        user_height = float(input("mata in höjd(mellan 27.5-38.5): "))         
        
        if  (user_width <= 15.5 or user_width >= 28.5):
            print(f"båda måste vara innanför intervallen, testa igen")
            continue    #go to next iteration of the loop, startar ett varv till

        if (user_height <= 27.5 or user_height >= 38.5):
            print(f"båda måste vara innanför intervallen, testa igen")
            continue    #go to next iteration of the loop, startar ett varv till

        break

    except ValueError:
        # Om annat än float
        print("bara siffror, tack")


#test data points from user input
test_data = {
    'width': [user_width],  # User data points' width
    'height': [user_height]  # User Test data points' height
}

#test data frame from USER INPUT
test_df = pd.DataFrame(test_data)
#-------------------------------------------------------------------------------------------

# KNN test data frame from USER INPUT 
test_df_knn = test_df

# ------------för att beräkna avstånd mellan testdata och originaldata, start---------------
# Function to calculate Euclidean distance----------
def euclidean_distance(row1, row2):
    return np.sqrt((row1['width'] - row2['width'])**2 + (row1['height'] - row2['height'])**2)

# --------------------------------- Uppgift 1 ---------------------

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






#------------------------------------------------------------------

# --------------------------------- Uppgift 2 ---------------------
# use KNN to get better classification (according to chatgpt), 10 data points instead of 1, based on majority vote
# K-Nearest Neighbors function (KNN)          
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
    print(f"Test point {i} ({test_point['width']}), {test_point['height']}) classified as {classification}")

    #Append the classification result
    classifications.append(classification)
#------------------------------------------------------------------

# KNN Add classification result
test_df_knn['label'] = classifications

# Scatter plot data for ORIGINAL DATA---------------------
pichu = df[df['label'] == 0]
pikachu = df[df['label'] == 1]

plt.scatter(pichu['width'], pichu['height'], color='blue', label='Pichu (label 0)')
plt.scatter(pikachu['width'], pikachu['height'], color='yellow', label='Pikachu(Not Pichu) (label 1)')
#----------------------------------------------------

# Scatter plot for USER test data points (classified as Test Pichu or Test Not Pichu)
test_pichu = test_df[test_df['label'] == 0]
test_not_pichu = test_df[test_df['label'] == 1]

plt.scatter(test_pichu['width'], test_pichu['height'], color='black', label='Test Pichu (label 0)')
plt.scatter(test_not_pichu['width'], test_not_pichu['height'], color='red', label='Test Not Pichu (label 1)')

# KNN Scatter plot data for TEST DATA of User input---------------------
test_pichu = test_df_knn[test_df['label'] == 0]
test_not_pichu = test_df_knn[test_df['label'] == 1]

plt.scatter(test_pichu['width'], test_pichu['height'], color='red', marker='x', label='KNN Test Pichu (label 0)')
plt.scatter(test_not_pichu['width'], test_not_pichu['height'], color='black', marker='x', label='KNN Test Not Pichu (label 1)')
#----------------------------------------------------






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
print("KNN Test Data Classification Results:")
print(test_df_knn)

#chatgpt-----------------------------------------------------------------------------------------------------------------------------------









