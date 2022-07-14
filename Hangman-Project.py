import random
import time

#list to pick words randomly for the plays to guess
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']


#asking user name 
name = input("Enter your name:")
#captalize converts the first character of a string to an 
#uppercase letter and all other alphabets to lowercase 
print("Hello", name.capitalize(), "let's start playing Hangman!")
#The sleep function suspends execution of the current thread
#for a given number of second 
time.sleep(1)
print("The objective of the game is to guess the secret word chosen by the computer.")
time.sleep(1)
print("You can guess only one letter at a time. Don't forget to press 'enter key' after each guess.")
time.sleep(2)
print("Let the fun begin!")
time.sleep(1)


wordList = random.choice(wordslist)
  
print("Guess the characters")
 
guesses = ''
 
# any number of turns can be used here
turns = 12
 
 
while turns > 0:
 
    # counts the number of times a user fails
    failed = 0
 
    # all characters from the input
    # word taking one at a time.
    for char in wordList:
 
        # comparing that character with
        # the character in guesses
        if char in guesses:
            print(char, end=" ")
 
        else:
            print("_")
            print(char, end=" ")
 
            # for every failure 1 will be
            # incremented in failure
            failed += 1
 
    if failed == 0:
        # user will win the game if failure is 0
        # and 'You Win' will be given as output
        print("You Win")
 
        # this print the correct word
        print("The word is: ", wordList)
        break
 
    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    print()
    guess = input("guess a character:")
 
    # every input character will be stored in guesses
    guesses += guess
 
    # check input with the character in word
    if guess not in wordList:
 
        turns -= 1
 
        # if the character doesn’t match the word
        # then “Wrong” will be given as output
        print("Wrong")
 
        # this will print the number of
        # turns left for the user
        print("You have", + turns, 'more guesses')
 
        if turns == 0:
            print("You Loose")