import numpy as np
import matplotlib.pyplot as plt

#1. Area
#Create a function that takes the base and height of
#  a triangle as input parameters and returns the
#  area of the triangle.

base = 2
height = 3
area = 0

def area_of_triangle(base, height):
    area = (base * height) / 2     
    return area

#call the function with the correct arguments:
area = area_of_triangle(base, height)

#then print the result
print(f"{area} kvm")

#detta verkar funka också:
def area_of_triangle():
    area = (base * height) / 2     
    return area

area = area_of_triangle()

#-------------
# 2. Euclidean distance (sort of like lab2)
#x,y for point one and two
point_one = [1, 2]
point_two = [3, 4]

#a)   Create a function that takes two points as input parameters
#  and return the Euclidean between them.
# Function to calculate Euclidean distance
# (between 2 data points)
# row1 first data point, row 2 second data point
def euclidean_distance(point_one, point_two):
    #float in front otherwise might see np.float64 in final output
    return float(np.sqrt((point_one[0]-point_two[0])**2+(point_one[1]-point_two[1])**2))

#call the function and store it in the var eucl
eucl = euclidean_distance(point_one, point_two)
print(eucl)

#b)
user_point1 = input("enter two digits, separated by a comma: ")
user_point2 = input("input two digits more, separated by a comma: ")
#split the input into x and y and convert them into float or int if needed
x1, y1 = map(int, user_point1.split(','))
x2, y2 = map(int, user_point2.split(','))
user_point1 = [x1, y1]
user_point2 = [x2, y2]

#funkar även om inte samma ord på parametrarna...
# the names of the variables you use when calling the function
#  don't need to match the parameter names in the function definition.
#  What matters is the order of the arguments.
user_eucl = euclidean_distance(user_point1, user_point2)
print(user_eucl)

#c)
# Use your function to calculate distances between
#  the origin (0, 0) and each of these points:
#  (10, 3), (-1, -9), (10, -10), (4, -2), (9, -10).
# hint: use a for statement

#initialize the list BEFORE the for loop
eucl_btw_dp_n_or = []

data_points = [(10, 3), (-1, -9), (10, -10), (4, -2), (9, -10)]
origin = [0,0]
print(data_points)

for i in data_points:
    new_eucl = euclidean_distance(origin, i) #i är den som ställer
    #sig på varje position i listan som anropas med for_loopen
    eucl_btw_dp_n_or.append(round(new_eucl, 1))

print(eucl_btw_dp_n_or)

#---------------

#3. make a function with def or lambda
# use def for more complex functions,
# use lambda for simple functions.



# using def

# 1. define the functions using def
#dont need "new" variables inside the function, except for x...
def f(x):
    return x**2 - 3 # f(x) = x^2 - 3

def g(x):
    return 4*x - 7 # g(x) = 4x - 7

# 2. generate x values for the plot, using NumPy's linspace function
x = np.linspace(-10, 10, 400) #400 about smoothness and details of graph
#the higher "400" u take the more details/smoothness u get

# 3. compute corresponding y-values for both functions
y_f = f(x)
y_g = g(x)

# 4. plot both functions on same graph
plt.figure(figsize=(8,6))
plt.plot(x, y_f, label='f(x) = x^2 - 3', color='blue')
plt.plot(x, y_g, label='g(x) = 4x - 7', color='red')

# 5. add title and labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph for f(x) and g(x)')
plt.legend()    #dont need to put parameters it will show anyway

# 6. display the plot
plt.grid(True)      # if want grid
plt.show()

# using lambda

# 1. define the functions using lambda function
f = lambda x: x**2 - 3
g = lambda x: 4*x - 7

# 2. generate x values to corresponding y
x = np.linspace(-10, 10, 400)

# 3. compute corresponding y values for each function
y_f = f(x)
y_g = g(x)

# 4. plot dongxi

plt.figure(figsize=(8,6))
plt.plot(x, y_f, color="green", label='f(x) = x^2 - 3')
plt.plot(x, y_g, color="red", label= '4x - 7')
plt.xlabel('x') 
plt.ylabel=('y')
plt.title('graph of f(x) and g(x)')
plt.legend()
plt.grid(True)
plt.show()
#-------------

# 5. name cleaner
# create a function that takes a name as an input 
# and removes all leading and trailing blank spaces, 
# and capitalizes the first letter of each name, 
# and makes the rest lowercase.


# 1. initialize var list

list_of_names1 = ["  MaRcUs ", " iDA aNderSon", "OLOF Olofsson            "  ]
list_of_names2 = list_of_names1

# 2. define function
def name_cleaner1(list_of_names1):
    modified_list1 = [i.strip().title() for i in list_of_names1]
    return modified_list1

# OR

def name_cleaner2(list_of_names2):
    modified_list2= [] #INITIALIZE THE FKKKNG LIST FIRST
    for i in list_of_names2:
        cleaned_name = i.strip().title() #kör både strip och capitalize samtidigt på listan
        modified_list2.append(cleaned_name)
    return modified_list2 #viktigt att inte sätta return inuti for loopen, inuti = bara ett varv i loopen körs


modified_list1 = name_cleaner1(list_of_names1)
modified_list2 = name_cleaner2(list_of_names2) #need to store the returned value then can print it
print(modified_list1)
print(modified_list2)

#-----------------------


