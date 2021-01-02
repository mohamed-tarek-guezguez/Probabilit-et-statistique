# *** GuezGuez Mohamed Tarek 2LM2 ***
from os import system
import random

# Global Variables
null = 0
compWins = 0
playerWins = 0

# Display Function
def choise():
    print('Choose One :\n\n\t1) Rock\n\t2) Paper\n\t3) Scissors\n')

# Random Conputer Choise Function
def conputerChoise():
    return random.randint(1, 3)

# Verification Player Choise Function
def verifPlayerChoise(x):
    if x == '1' or x == '2' or x == '3' or x == 'R' or x == 'P' or x == 'S' or x == 'ROCK' or x == 'PAPER' or x == 'SCISSORS': 
        return True
    else:
        return False

# int Player Choise Function
def intInput(x):
    if x == '1' or x == 'R' or x == 'ROCK':
        return 1
    elif x == '2' or x == 'P' or x == 'PAPER':
        return 2
    else:
        return 3
    
# Player Choise Function
def PlayerChoise():
    x = input('Your Choose : ')
    while(not(verifPlayerChoise(x.upper()))):
        x = input('Your Choose : ')
    return intInput(x.upper())

# Computer Or Player Win
def win(c, p):
    if c == p:
        return 'null'
    elif (c == 1 and p == 3) or (c == 2 and p == 3) or (c ==3 and p == 2):
        return 'c'
    else:
        return 'p'

# Str Player & Computer Choise Function
def strInput(x):
    if x == 1:
        return 'ROCK'
    if x == 2:
        return 'PAPER'
    if x == 3:
        return 'SCISSORS'

# verif test function
def varifTest(t):
    if t == '':
        return True
    else:
        return False

# Start Player Function
def play():
    test = True
    while test:
        system('cls')
        choise()
        compChoice = conputerChoise()
        playerChoice = PlayerChoise()

        print('Your Choise : ' + strInput(playerChoice) + ' | Computer Choise : ' + strInput(compChoice))
        w = win(compChoice, playerChoice)
        if w == 'null':
            print('*** Null ***')
            global null
            null += 1
        if w == 'c':
            print('*** Computer Win ***')
            global compWins
            compWins += 1
        if w == 'p':
            print('*** Player Win ***')
            global playerWins
            playerWins += 1

        test = varifTest(str(input('\nPress enter to continue... ')))
    print('\nComputer :', compWins, ' Player :', playerWins, ' Null :', null)

play()
