from gameComponents import gameVars

def my_function():
    if gameVars.computer_choice == gameVars.player_choice:
            print("-_-_-_-_-_-_-_-_-_-_ !Equal! -_-_-_-_-_-_-_-_-_-_-_-\n")
    elif gameVars.computer_choice == "rock":
        if gameVars.player_choice == "scissors":
            gameVars.player_lives -= 1
            print("you lose! player lives:", gameVars.player_lives)
        else:
            print("-_-_-_-_-_-_-_- Hoooooray !You win! -_-_-_-_-_-_-_-\n ")
            gameVars.computer_lives -= 1
    elif gameVars.computer_choice == "paper":
        if gameVars.player_choice == "rock":
            gameVars.player_lives -= 1
            print("you lose! player lives:", gameVars.player_lives)
        else:
            print("-_-_-_-_-_-_-_- Hoooooray !You win! -_-_-_-_-_-_-_-\n ")
            gameVars.computer_lives -= 1
    elif gameVars.computer_choice == "scissors":
        if gameVars.player_choice == "paper":
            gameVars.player_lives -= 1
            print("you lose! player lives:", gameVars.player_lives)
        else:
            print("-_-_-_-_-_-_-_- Hoooooray !You win! -_-_-_-_-_-_-_-\n ")
            gameVars.computer_lives -= 1

