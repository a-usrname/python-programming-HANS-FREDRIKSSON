import random
# for statements

# 1. Count numbers
# use a for statement to count from -10 to 10 with one increment
# a)
for i in range(-10, 11):
    print(i)
    
# b)
for i in range(-10, 11, 2): #2:an gör att det blir vartannat från -10, 
# alltså varje even number i detta fall
    print(i)

# 2. arithmetic sum
# for statement
# a) summa för 1-100
sum = 0
for i in range(1, 101):
    sum += i
print(sum)
# b) summa för 1 - 99 bara udda tal
sum = 0
for i in range(1, 100, 2): #2:an ger vartannat tal, i detta fall udda tal
    sum += i
print(sum)

# multiplication table
# a) print out the 6th multiplication table from 0 to 10

user_input_number = int(input(f"number btw 1-10: "))
user_input_start = int(input(f"start: "))
user_input_stop = int(input(f"stop: "))
user_input_stop = user_input_stop + 1

for i in range(user_input_start, user_input_stop):
    print(f" {user_input_number} x {i} = {user_input_number * i}")

# b) 
# print out a full table of 0-10 x 0-10 
for i in range(0, 11):  # Loop through rows (0 to 10)
    for j in range(0, 11):  # Loop through columns (0 to 10)
        print(f"{i * j:4}", end=" ")  # Print multiplication result in a matrix format, aligned by width 4
    print() 

# 4. Faculty
# use a for statement to compute n! 
# n! = 1*2*3 ... *(n-1)*n
# let the user input n
n = int(input(f"input value for n: "))  #n value
factorial = 1 # set to 1 as multiplying by 1 doesnt affect the value

for i in range(1, n + 1): #loop from 1 to n (inclusive)
    factorial *= i # multiply factorial by i at each step

print(f"the factorial is {factorial}")

# 4. computer guess the number

#step 1 make a random int btw 1000 and 9999
slumptal = random.randint(1000, 9999)
print(slumptal)

# Step 2: Use a for loop to guess the correct number
for guess in range(1000, 10000):  # Loop through all four-digit numbers
    #if guess != slumptal:
        #print(guess)
    
    if guess == slumptal:
        print(f"Correct guess! The number is {guess}")
        break






