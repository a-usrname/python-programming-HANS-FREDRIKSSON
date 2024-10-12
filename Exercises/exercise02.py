import random


# 1. Count numbers (*)
# Use a while statement to count from -10 to 10 with one increment.

# Hint
# i += 1 # adds one and assigns it to i, equivalent to i = i + 1

number = -10

while number < 11:
    print(number, end=" ")
    number += 1

# 2. Arithmetic sum (*)
# Use a while statement to compute the following sums:
# a) sum = 1+2+...+99+100
# from chatgpt---------
# Initialize variables
i = 1
total_sum = 0

# While loop to compute the sum
while i <= 100:
    total_sum += i  # Add i to the total sum
    i += 1          # Increment i with 1

# Print the result
print("")
print("Sum =", total_sum)
#--------------

# b)
# sum = 1+3+5+...+97+99
i = 1
total_sum = 0

while i <= 99:
    total_sum += i
    i += 2          #eftersom 2 steg emellan/udda tal

print("Sum =", total_sum)

# 3. Guess number game (*)

#Behöver declare random variabeln här för att ha inuti funktionerna sen
random_number = random.randint(1, 100)
print(random_number)

def game_user_guess(random_number):
    user_guess_count = 0
    #random_number = get_random() # här blir ett nytt random nummer...
    
    while True:               
        
        user_guess = input(f"Gissa på ett tal mellan 1 och 100(nuvarande antal gissningar {user_guess_count}: ")
        
        try:
            user_guess = int(user_guess)
                
            if user_guess > 100 or user_guess < 1:
                print("Inte lägre än 1, inte högre än 100.")
                continue
            print(f"Du gissade på {user_guess}.")
            #kanske kan lägga dessa nedanför except så att slipper göra ny random nummer?
            if user_guess < random_number:
                print("Du gissade fel, det var för lågt. Gissa högre!")
                user_guess_count += 1
                continue
            if user_guess > random_number:
                print("Du gissade för högt, gissa lägre!")
                user_guess_count += 1
                continue
            else:
                user_guess_count += 1
                print(f"Det var rätt! Du gissade på {user_guess} och talet var {random_number}! \nDu gissade {user_guess_count} gånger.")
            break
        
        except:
            print("Enbart siffor, tack.")
         
    return user_guess_count

 #b) Make an algorithm to automatically guess the correct number. Can you optimize to get as few guesses as possible? (**)
 # Hint Half your testing number each time
#according to chatgpt: binary search algorithm, which is optimal for guessing a number within a known range
# binary search algorithm will divide the search interval after each wrong guess, and next guess in the middle

def algorithm_guess(random_number, low=1, high=100):
    alg_guess_count = 0
    alg_guess = 0
    
    while low <= high:
        # guess the middle number
        alg_guess = (low + high)//2
        alg_guess_count += 1

        print(f"Algo guessed {alg_guess}")

        if alg_guess == random_number:
            print(f"Algo guessed correct in {alg_guess_count} attempts.")
            return alg_guess_count
        
        #adjust the RANGE if the guess is too low, to prevent the algo from guessing the same number again
        elif alg_guess < random_number:
            print(f"Algo guessed {alg_guess} which is too low.")
            low = alg_guess + 1
        
        #adjust the RANGE if the guess is too high
        else: 
            print(f"Algo guessed {alg_guess} which is too high.")
            high = alg_guess - 1

    return alg_guess_count

def compare(alg_guess_count, user_guess_count):
    if alg_guess_count > user_guess_count:
        print(f"Du gissade rätt med FÄRRE antal försök({user_guess_count}) än Algo({alg_guess_count})!\nSå du vann!")
    elif alg_guess_count < user_guess_count:
        print(f"Du gissade rätt med FLER antal försök({user_guess_count}) än Algo({alg_guess_count})!\nSå du förlorade!")
    else:
        print(f"Oavgjort. Algo hade {alg_guess_count} och du hade {user_guess_count}.")

    return None

#remove the # below to start game
# start game for user, and use random_number, and store the result in user_guess_count
#user_guess_count = game_user_guess(random_number)
# start game for the algorithm, and use random_number, and store the result in algo_guess_count
#alg_guess_count = algorithm_guess(random_number)
#compare user guess count with algo's, see whos the winner
#compare(alg_guess_count, user_guess_count)

# nu funkar det^^^

# 4. Create a multiplication game

# function to randomize x and y from 1 to 10
def a_random_number():
    random_x_or_y = random.randint(1,10)
    print(random_x_or_y)
    return random_x_or_y

#b)   Add a menu for choosing difficulty level of the game
def difficulty_level():  
    stop_guessing = 0
    while True:
        
        choice = int(input("please choose a difficulty level: \n1. Hard level: You get 3 guesses.\n2. Medium level: 7 guesses. \n3. Easy: 20 guesses. Please select 1, 2 or 3."))
        if choice == 1:
            stop_guessing = 3
            break
        elif choice == 2:
            stop_guessing = 7
            break
        elif choice == 3:    
            stop_guessing = 20
            break
        else: 
            print("pls choose 1, 2 or 3")
            continue
    return stop_guessing

allowed_number_of_guesses = difficulty_level() #fix so that can be used inside game

print(allowed_number_of_guesses)

def game():
    user_score = 0
    
    while True:
        
        random_x =a_random_number()
        random_y = a_random_number()
        result = random_x * random_y
        
        user_answer = int(input(f"what is {random_x} multiplied with {random_y}?"))
        if user_answer == result:
            print(f"good, correct, answer is {result}!")
            user_score += 1
        else:
            print(f"wrong, correct answer is {result}.")

        play_again = input("wanna try again? yes/no?")
        if play_again == "no":
            print(f"Ok, see you next time! Your total score is: {user_score}")
            break
        else:
            continue
    return None

a_random_number()
game()

# 5.


    




