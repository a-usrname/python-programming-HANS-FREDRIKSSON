import numpy as np
import matplotlib.pyplot as plt

# 1. find errors in the code to compute
#  the distance between the point (x,y) and the origin 
# in a cartesian coordination system (det vanliga koord.systemet)

#distance formula = pythagoras sats för hypotenusan
def distance(x,y):
    return np.sqrt(x**2+y**2)

print(distance(0.5,0.5))
#-------------------------------

# 2. Find the errors in this code. Just change the
#  function, don't touch the test program.
#Hint
#Print out and test different cases to build up the
#  condition in the if-statement
def is_fourdigit(number):
    if number//1000 < 10:
        return True
    else:
        return False

# test program
test_numbers = [231, 3124, -4124, -1000,-999, 1001, 10000, -10000, 999]

for number in test_numbers:
    if is_fourdigit(number):
        print(f"{number} is four-digit")
    else:
        print(f"{number} is not four-digit")
#------------------

# 4. Tram

#Write a program to prompt the user for:

#number of times he/she wants to take tram in one month
#cost for one ticket
#cost for monthly card

#trams_per_month = int(input("times of trams per month (2 per day?): "))
cost_per_ticket = 10
cost_monthly_card = 270

while True:

    try:
        trams_per_month = int(input("times of trams per month (2 per day?): "))
        if trams_per_month < cost_monthly_card:
            print(f"you should buy one way tickets, \na monthly card is more expensive, \nsince u dont travel that much.")

        else:
            print(f"you should buy a monthly ticket, one way tickets are more expensive for u\nsince u travel that much.")

        break

    except ValueError:
        print("only digits, not other characters. try again!")
    
#------------------------

# 