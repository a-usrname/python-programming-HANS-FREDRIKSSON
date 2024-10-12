#chatgpt (havent changed it)
# This file contains the function to check if a point is above/right or below/left of the line

def point_position(x, y, k, m):
    """
    Function to determine if a point (x, y) is above/right, below/left, or on the line y = kx + m.
    Args:
    x (float): The x-coordinate of the point.
    y (float): The y-coordinate of the point.
    k (float): The slope of the line.
    m (float): The y-intercept of the line.

    Returns:
    str: A string indicating the position of the point relative to the line.
    """
    # Calculate the predicted y value from the line equation
    predicted_y = k * x + m
    
    # Compare the actual y with the predicted y
    # ska vara som i labb2 med 0 eller 1
    if y > predicted_y:
        #return "above/right"
        return 1
    
    else:
        return 0
    #elif y < predicted_y:
        #return "below/left"
        #return 0
    #else:
        #return "on the line"
