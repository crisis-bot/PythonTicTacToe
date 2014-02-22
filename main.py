# Created By: Omar Quazi - 576314
# TicTacToe Program.... A try... Second Attempt actually.
# Copyright under the GNU GPL v3. Enjoy :)

import random

def mainBoard(p):
    # Print the current board setup now. Or in other words
    # the tic tac toe game, current setup. Wat eva' you get
    # what I mean.
    print p[0]+" | "+p[1]+" | "+p[2],"\n"
    print p[3]+" | "+p[4]+" | "+p[5],"\n"
    print p[6]+" | "+p[7]+" | "+p[8],"\n"

def getPosition(p):
    # Where does the user want to put their mark?
    where = input("Where do you want to place your mark? ")
    # is a X/Y already in that spot?
    while ("Y" in p[where-1]) or ("X" in p[where-1]):
        # If so, ask again.
        where = input("Place is already covered. Please try again:\n")

    # RETURN IT! :D
    return where

def placeValues(letter, where, p):
    # Well, now that check is done, put it into place.
    # Remember, the user doesn't really know about the ZERO
    # place value in a list, therefore, you must MINUS
    # ONE from the "where" Variable.
    p[where-1] = letter

    # RETURN IT! :P
    return p

def winnerCheck(p,compLetter,playerLetter):
    # Return Possible: [1,2,3]
    # 1 = Player Wins
    # 2 = Computer Wins
    # 3 = A TIE!
    # 4 = NOTHING YET!
    winner = 4

    # Complex, but makes sense, ain't got time to explain.
    if (p[0] == "X" or p[0] == "Y") and (p[1] == "X" or p[1] == "Y") and (p[2] == "X" or p[2] == "Y") and (p[3] == "X" or p[3] == "Y") and (p[4] == "X" or p[4] == "Y") and (p[5] == "X" or p[5] == "Y") and (p[6] == "X" or p[6] == "Y") and (p[7] == "X" or p[7] == "Y") and (p[8] == "X" or p[8] == "Y"):
        winner = 3

    # Check for to combinations, is there a winner?    
    if p[0] == p[1] == p[2]:
        winner = p[0]
    elif p[3] == p[4] == p[5]:
        winner = p[3]
    elif p[6] == p[7] == p[8]:
        winner = p[6]
    elif p[0] == p[3] == p[6]:
        winner = p[0]
    elif p[1] == p[4] == p[7]:
        winner = p[1]
    elif p[2] == p[5] == p[8]:
        winner = p[2]
    elif p[0] == p[4] == p[8]:
        winner = p[0]
    elif p[2] == p[4] == p[6]:
        winner = p[2]

    # Well, is the winner X?
    if winner == "X":
        # If so, is it the computer that has the X value?
        if compLetter == "X":
            winner = 2
        else: # If not, just assign player/user as winner.
            winner = 1
    # Well, what about Y?
    elif winner == "Y":
        # If so, is it the computer that has the Y value?
        if compLetter == "Y":
            winner = 2
        else: # If not, just assign player/user as winner.
            winner = 1

    # RETURN IT! :P
    return winner

# A GENERIC List Setup.
places = ["1","2","3","4","5","6","7","8","9"]

# Who should go FIRST?
turn = random.randint(1,2)

# Then assign letters accordingly
if turn == 1:
    playerLetter = "X"
    compLetter = "Y"
else:
    playerLetter = "Y"
    compLetter = "X"
# Setup a turn variable with True and False
# You will see why, you cannot do the inverse of turn
# this is because, it is a number. If it is a True or False value
# then it can easily be inversed. This variable will be used
# for taking turns. Run through the program to understand it.
if turn == 1:
    whosTurn = True
elif turn == 2:
    whosTurn = False

# Print the main board
mainBoard(places)

# This is just the first WELCOME message. Example, since this is False
# when it enters the While loop, it will not print mainBoard, because
# if there is no welcome trigger, the game board is printed more than once
# without any moves shown. Which confuses the user. If you still need more
# info, ask me. Or for testing, make it True, watch what happens. :)
welcome = False

# Just setup a trigger to continue or exit.
game = True

# Main loop.
while game:
    # Now that it is false, it will not print the game board more than
    # once.
    if welcome:
        mainBoard(places)

    # If whosTurn is TRUE, or in other words it is the players turn
    # run this:
    if whosTurn:
        print "-- Your Turn --"
        # Get position from user:
        position = getPosition(places)
        # Now, place it into the main places list
        places = placeValues(playerLetter, position, places)
    else: # And if it is false, it is the computers turn. :)
        print "-- Computers Turn --"
        # Randomly generate a position
        position = random.randint(1,9)
        # What if the position is already taken?
        while ("Y" in places[position-1]) or ("X" in places[position-1]):
            # Generate AGAIN if the place is taken.
            position = random.randint(1,9)
        # Now simply put the computers letter into the place. :)
        places[position-1] = compLetter

    # Call the winner function
    aWinner = winnerCheck(places,compLetter,playerLetter)

    # Check the winner codes/comments inside the winner function
    if aWinner < 4:
        game = False

    # Turn whosTurn the opposite of what it is, so that
    # we can alternate turns. :P
    whosTurn = not whosTurn
    
    # Now turn welcome ON, so that from now on, it prints the main board.
    welcome = True



# Out of the main loop, print the main board so the user sees it and
# understands.
mainBoard(places)

# If the winner code is ONE, user WINS!
if aWinner == 1:
    print "YOU WON! GOOD JOB! Now, for a victory party. :)"
elif aWinner == 2: # If the code is TWO, computer wins!
    print "Ha ha, looser, the COMPUTER WON! Try again."
else: # Else, it's a TIE!
    print "It was a TIE! Play again!"
