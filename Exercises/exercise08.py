import random
# 1. Dice rolls (*)
# Create a textfile called dice_rolls.txt using Python. 
# Also for each subtask, write adequate headers.
# a)   Simulate 20 dice rolls and write them to your textfile. (*)

#dice_roll = random.randint(1,6) #läggs den här blir det bara EN random

#dice_roll = random.randint(1,6) läggs den här så blir det bara EN random dice_roll 
dice_total= []  #skapa först innan for loopen
antal_dice = 0

for i in range(20):     #i går igenom for loopen med 20 ggr
    dice_roll = random.randint(1,6)  
    dice_total.append(dice_roll)       # för varje varv läggs dice_roll till i dice_total
    antal_dice += 1
print(dice_total, antal_dice)

#for txt file:



# list of items is in dice_total[]
# open (dont need to "create" it first) and then write to it
with open('txt_file_from_dice_total.txt', 'w') as file: #w = overwrite the file
    # write header
    file.write('list of dice rolls\n') # adds the header
    file.write('------------------\n') # a line to separate nidnoi

    #put the list items, row by row
    for i in dice_total:
        # obs file.write expects a str list, not an int list, 
          file.write(str(i) + ' ')    #i is the number and \n to jump to next line
    
# b)   Sort the dice rolls from a) and write them to a separate row in the same textfile. (*)
dice_total.sort()

with open('txt_file_from_dice_total.txt', 'a') as file: #a append in the file
     #append the list items, row by row
    file.write('\n') # the appended context below is placed on a new line
    for i in dice_total:
        # obs file.write expects a str list, not an int list, (dont need the str below again)
          file.write(str(i) + ' ')    #i is the number and \n to jump to next line
    
# c)   Count the number of fours in the dice rolls and write them to a separate row in the same textfile. (*)
number_of_fours = 0

with open('txt_file_from_dice_total.txt', 'a') as file: #a append in the file
     #append the list items, row by row
    file.write('\n') # the appended context below is placed on a new line
    for i in dice_total:
        if i == 4:
          number_of_fours += 1
        
    # obs file.write expects a str list, not an int list, 
    file.write(str(number_of_fours) + ' ')    #i is the number and \n to jump to next line
    
