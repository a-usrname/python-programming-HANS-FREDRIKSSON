import random
import matplotlib.pyplot as plt

#1. Dice rolls (*)
#Simulate 10 dice rolls and append the rolls to a list or use list comprehension.
#def make_dice_roll():
#    dice_roll = random.randint(1, 6)
#    return dice_roll

the_list = []

for i in range(1,11):
    dice_roll = random.randint(1, 6)
    the_list.append(dice_roll)
print(the_list)    

  # a)   sort the list in ascending/stigande order (*)
the_list.sort()
print(the_list)

  # b)   sort the list in descending/fallande order (*)
the_list.sort(reverse=True)
print(the_list)

  # c)   find the maximum and minimum value in the list (*)
min_value = min(the_list)
max_value = max(the_list)
print(min_value, max_value)

# 2. Food menu
#a)
matlista = ["vegetarisk lasagne", "spaghetti", "fisk", "grönsakssoppa", "pannkakor"]
#b)
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
#c) using ZIP to combine lists

menu_for_the_week = [f"{day}: {meal}" for day, meal in zip(weekdays, matlista)]

print(menu_for_the_week) #prints everyting on one line
for menu in menu_for_the_week:
    print(menu)             #prints one day/meal per line, better formatting

# 3. Squares
# a) list comprehension


the_list = []

for i in range(-10, 11):
    kvadrerat_tal = i**2
    the_list.append(kvadrerat_tal) #append lägger till på slutet av listan
print(the_list)

#plt.plot(the_list)
plt.plot(the_list)
plt.ylabel("y")
plt.xlabel("x")
plt.title("the function of x^2")
plt.show()

#5. dice rolls convergence/sammanfallande
#a)   100 dice rolls and count the number of outcome six. 
dice_rolls =[]

for i in range(1, 101):
    sth = random.randint(1, 6)
    dice_rolls.append(sth)
print(dice_rolls)

print(len(dice_rolls)) #se hur många ggr for loopat dice_rolls (len = length)

antal_sexor = 0

for i in dice_rolls:
    if i == 6:
        antal_sexor += 1
print(antal_sexor)

#b) ...

#
