#chatgpt (havent changed it, except for return 1 and 0)
# This file contains the function to check if a point is above/right or below/left of the line

def point_position(x, y, k, m):
    # Calculate the predicted y value from the line equation
    predicted_y = k * x + m
    
    # Compare the actual y with the predicted y
    # ska vara som i labb2 med 0 eller 1
    if y > predicted_y:
        #return "above/right"
        return 1
    
    else:
        #if not "above/right"
        return 0

