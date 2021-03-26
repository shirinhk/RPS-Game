from random import randint

from gameComponents import gameVars, winLose, compare

while gameVars.player_choice is False:
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    print("-_-_-_-_-_-_-_-_-_-_   Let's Play   -_-_-_-_-_-_-_-_-_-_")
    print("-_-_-_-_-_-_-_-_   ROCK PAPER SCISSOR   -_-_-_-_-_-_-_-_\n")
    print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n")
    print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n")
    print("Choose your weapon! Or type quit to exit\n") #\n means "new line"
    gameVars.player_choice = input("Choose rock, paper, or scissors: \n")

    if gameVars.player_choice == "quit":
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        print(" oh no!!!!!!  You chose to quit, come back soon :) ")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        exit()

    gameVars.computer_choice = gameVars.choices[randint(0, 2)]

    print("user chose: " + gameVars.player_choice)
    print("computer chose: " + gameVars.computer_choice)

    compare.my_function()

    if gameVars.player_lives == 0:
        winLose.winorlose(" ))))))))))): lost :((((((((( ")
    elif gameVars.computer_lives == 0:
        winLose.winorlose(" (((((((((((:  won  :)))))))))")
    else:
        gameVars.player_choice = False

