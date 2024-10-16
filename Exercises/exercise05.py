#1. counting letters

user_input = input("write a word using both upper and lower case letters, hit enter!")
#a) print the number of letters in the word
number_of_letters = len(user_input) #len returns the number of characters in the string in this case
#len is for length ffs
print(number_of_letters)

#b) count upper and lower case letters in the word
# initialize counters/vars for number of upper and lower case letters
upper_case_letters = 0
lower_case_letters = 0

# loop through each character of the word
for char in user_input: #char is what is ususally i 
    if char.isupper():          #isupper = function for check if upper case
        upper_case_letters += 1
    else:
        lower_case_letters += 1

print(f"no of lower case letters: {lower_case_letters}\nno of upper case letters: {upper_case_letters}")

# so isupper = count upper case letters
# and islower = count lower case letters


# 2. Count the number of words in a sentence
sentence = "A picture says more than a thousand words, a mathematical formula says more than a thousand pictures"
#split the string into words(using spaces as a default delimiter) and put them as a list instead
word_count = len(sentence.split())
print(word_count)

#3. Palindrome (samma bakåt/framåt)
#let the user input a word and check if its a palindrome
user_word = input(f"A palindrome is spelled the same both ways. Enter a word and hit enter to check: ")
#reverse a word in python using slicing:
user_word_reversed = user_word[::-1] #[::-1] reverses the word's spelling
print(user_word_reversed)

if user_word == user_word_reversed:
    print("thats a palindrome")
else:
    print("thats not a palindrome") 
 

 #4. counting VOWELS in the sentence

sentence = "Pure mathematics is, in its way, a poetry of logical ideas"
no_of_vowels = 0

vowels = "aeiouyAEIOUY" #define set of vowels

#loop through each character in the string
for char in sentence:   #char/i kommer gå igenom sentence
    if char in vowels:  #och kolla om char finns i vowels
        no_of_vowels += 1

print(no_of_vowels)



