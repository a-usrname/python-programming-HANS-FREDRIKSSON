# 1. Pythagorean Theorem
# a) A right angled triangle has the catheti: a = 3 and b = 4 length units.
# Compute the hypothenuse of the triangle. (*)
import math
a = (3)
b = (4)
hypothenuse = math.sqrt(a**2 + b**2)
print(f"Answer: The hypothenuse is {hypothenuse} length units.")

# b) A right angled triangle has hypothenuse c = 7.0 and a cathetus a = 5.0 length units.
#  Compute the other cathetus and round to one decimal. (*)
a = 5**2
c = 7**2
# round(number, 1) avrundas till en decimal
b = round((math.sqrt(c - a)),1)

print(f"Answer: The cathesis b is {b} length units.")   

# 2. Classification accuracy (*)
# A machine learning algorithm has been trained to predict whether or not it would rain the next day.
# Out of 365 predictions, it got 300 correct, compute the accuracy of this model.
accuracy = round((300/365), 3)
print(f"The answer is: {accuracy}")

# 3. Classification accuracy (*)
# A machine learning model has been trained to detect fire.
# Here is the result of its predictions:

tp = 2
fp = 2
fn = 11
tn = 985
accuracy = round((tp+tn)/(tp+tn+fp+fn), 3)
print(f"The answer is: {accuracy}")

# 4. Line (*)
# Compute the slope k and the constant term m of the line with points A:(4,4) and B:(0,1)
k = (1-4)/(0-4)
# y = kx + m 
y = 4
x = 4
m = round(y-k*x, 2)
print(f"k is {k} and m is {m}, so the equation for the slope is y = 0.75x + 1")

# Euclidean distance (*)
# The Euclidean distance between the points P1 and P2 is the length of a line between them. 
# Let P1: (3,5) and P2: (-2,4) and compute the distance between them.
distance = round(math.sqrt(((-2-3)**2)+((4-5)**2)), 1)
print(f"The distance is around {distance} length units.")

# 6. Euclidean distance in 3D (**)
# Calculate the distance btw the points P1: (2,1,4) and P2: (3,1,0).

distance = round(math.sqrt(  (2-3)**2 + (1-1)**2 + (4-0)**2 ), 2)
print(f"The 3D distance is around: {distance} l.u.")
