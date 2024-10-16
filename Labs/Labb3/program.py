import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#CLEAN UP THE CODE AND COMMENTS BEFORE

# from chatgpt


# Import the point_position function from position_utils.py
from function import point_position

# Load the data from the CSV file
df = pd.read_csv('unlabelled_data.csv')
df.columns = ['x', 'y']

# Fit a Linear Regression Line Using Numpy
# 1 specifies you're fitting a linear equation (a straight line).
k, m = np.polyfit(df['x'], df['y'], 1)

# Print the slope (k) and intercept (m)
print(f"Slope (k): {k}")
print(f"Y-intercept (m): {m}")

# Apply the function to each data point in the DataFrame and add a new column with the result
# (axis1 to use the function across the columns for each row)
#df['position'] = df.apply(lambda row: point_position(row['x'], row['y'], k, m), axis=1) 
df['position'] = df.apply(lambda row: point_position(row['x'], row['y'], k, m), axis=1) 
# kanske position: 0 = below/left, 1 = above/right

# Print the DataFrame with the new 'position' column
# now df has 3 columns (x, y, position)
print(df)

# Create a scatter plot of the data points
#plt.scatter(df['x'], df['y'], color='blue', label='Data points')

#test, gör om dessa i funktionen så 0, 1 ? 
# som i pikachu labben? kanske kan göra om rad 26 till abo/righ = 0, bel/lef = 1?
above_right = df[df['position'] == 1]
below_left = df[df['position'] == 0]

plt.scatter(above_right['x'], above_right['y'], color='blue', label='above/right (1)')
plt.scatter(below_left['x'], below_left['y'], color='yellow', label='below/left (0)')


# Plot the best-fit line
plt.plot(df['x'], k * df['x'] + m, color='red', label=f'Best fit line: y = {k:.2f}x + {m:.2f}')

# Add labels, title, and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot with Best-Fit Line')
plt.legend()

# Show the plot
plt.show()

# source: https://pandas.pydata.org/docs/user_guide/10min.html)
# saves the 3 columned data frame (columns: x, y, position) as a .csv
df.to_csv("labelled_data.csv")

# plot the data points, their class, and the line




