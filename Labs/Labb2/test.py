import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


#chatgpt-----------------------------------------------------------------------------------------------------------------------------------

# To get original data and user input data

# Read the original data file (Pichu and Pikachu data), skipping the first line
df = pd.read_csv('datapoints.txt', skiprows=1, header=None)

# Assign column names to the data frame: 'width', 'height', 'label'
df.columns = ['width', 'height', 'label']


#user input for test point-----------------------------------------------------------
# while loop for handling input other than float
user_width = 0
user_height = 0


def get_user_input():
    
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
        
    return user_width, user_height
    

#test data points from user input
test_data = {
'width': [user_width],  # User data points' width
'height': [user_height]  # User Test data points' height
}

get_user_input()


    # test data frame from USER INPUT
test_df = pd.DataFrame(test_data)

    # KNN test data frame copy from USER INPUT 
test_df_knn = test_df

    

#-------------------------------------------------------------------------------------------


print(test_df, test_df_knn)

