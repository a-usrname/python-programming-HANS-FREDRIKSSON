import pandas as pd
import matplotlib.pyplot as plt
import numpy as np #betyder att den inte används just nu ...

# Laboration3 - linjär klassificering

# df data frame for the unlabelled data
df = pd.read_csv('unlabelled_data.csv')#, dtype={'X': 'float64', 'Y': 'float64'})
df.columns = ['x', 'y']

print (df)

#--------------chatgpt ang. b)
# Fit a Linear Regression Line Using Numpy:
# Use numpy's polyfit to fit a line to the x and y columns in the DataFrame
k, m = np.polyfit(df['x'], df['y'], 1)

# Print the slope (k) and intercept (m)
print(f"Slope (k): {k}")
print(f"Y-intercept (m): {m}")

#-----
# Create a scatter plot of the data points
plt.scatter(df['x'], df['y'], color='blue', label='Data points')

# Plot the best-fit line
plt.plot(df['x'], k * df['x'] + m, color='red', label=f'Best fit line: y = {k:.2f}x + {m:.2f}')

# Add labels, title, and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot with Best-Fit Line')
plt.legend()

# Show the plot
plt.show()

#-------------
# c)

