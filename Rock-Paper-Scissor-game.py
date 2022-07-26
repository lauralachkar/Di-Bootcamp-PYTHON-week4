#we import randint from the random module. 
# #Because our opponent will be the computer
# from random import randint

# #create a list of play options : rock paper or scissors 
# #three possibilities plays for the player and the computer 
# #on each turn
 t = ["Rock", "Paper", "Scissors"]

# #assign a random play to the computer
# #as you know the computer starts to count from zero
# #so "Rock" wil be in the 0 position 
# #the "Scissors" will be in the 1 position and so on
computer = t[randint(0,2)]

# #set player to False
player = False

while player == False:
# #set player to True
     player = input("Rock, Paper, Scissors?")
     if player == computer:
         print("Tie!")
     elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
        elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
        elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
             print("You win!", player, "cut", computer)
        else:
            print("That's not a valid play. Check your spelling!")
     #player was set to True, but we want it to be False so the loop continues
            player = False
            computer = t[randint(0,2)]


# #the computer will patiently wait for you to make a play
# #when the loops starts

# #When we take our turn,our status changes from False to True because any 
# #value assigned to the variable player makes player True

# #input fucntion to pass the new value to the variable player.

# #we check every possible outcome of the game and return a message 
# # stating the winner, a tie, or an error in if/elif/else statements

# #Finally we reset the player value to False to restart the while loop.


