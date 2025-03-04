# Day-4 project - Rock,Paper,Scissors
import random

print("Lets Play Rock,Paper,Scissors!")
game_round = 0
player_score = 0
comp_score = 0
game_options = ["Rock", "Paper", "Scissors"]
while game_round < 3:
    player_choice = int(input("insert number:\n1.Rock\n2.Paper\n3.Scissors\nyour answer ")) - 1
    if player_choice not in [0,1,2]:
        print("Invalid Input! Game Over!")
        exit(0)
    comp_choice = random.choice(game_options)
    if game_options[player_choice] == comp_choice:
        print(f"both you and the computer choose {comp_choice}")
        print("Its a draw! continue...")
    else:
        print(f"Player choose --> {game_options[player_choice]}")
        if game_options[player_choice] == game_options[0]:
            print(f"Computer choose --> {comp_choice}")
            if comp_choice == game_options[1]:
                print("computer win this round!")
                comp_score += 1
            elif comp_choice == game_options[2]:
                print("player win this round!")
                player_score += 1
        elif game_options[player_choice] == game_options[1]:
            print(f"Computer choose {comp_choice}")
            if comp_choice == game_options[2]:
                print("computer win this round!")
                comp_score += 1
            elif comp_choice == game_options[0]:
                print("player win this round!")
                player_score += 1
        else:
            print(f"Computer choose {comp_choice}")
            if comp_choice == game_options[0]:
                print("computer win this round!")
                comp_score += 1
            elif comp_choice == game_options[1]:
                print("player win this round!")
                player_score += 1

        game_round += 1


print(f"Player score = {player_score}  |   Computer score = {comp_score}")
if comp_score <= player_score:
    print("Player win!")
else:
    print("Computer win!")

