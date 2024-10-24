# dictionary exercises

# 1. Curriculum
#Create a dictionary containing all the courses
#  that you will study in this program,
#  with the course names as KEYS and the amount
#  of points as VALUE. Then calculate the number
#  of points that you will study in total.

# Create a dictionary with subjects and their values
curriculum = {"course1": 5,
              "course2": 10, 
              "course3": 5 
}

# calculate the total value, sum the values
calculate = sum(curriculum.values())

print(calculate)

#---------------------
# Simulate 1000000 dice rolls and save the number of ones, twos, ..., sixes in a dictionary.
#  Then print them out in the terminal.

# Initialize the dictionary to hold counts of dice outcomes
dice_rolls_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

for i in range(1000000):
    dice_roll = random.randint(1,6)
    dice_rolls_dict[dice_roll] += 1

for number, antal in dice_rolls_dict.items():
    print(f"number of {number}s: {antal}")