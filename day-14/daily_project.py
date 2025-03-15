import random

from art import game_logo
from Database import quantities_dict


player_score = 0
question_n = 1

first_quan = ""
second_quan = ""

game_flag = True

key_list = list(quantities_dict.keys())

print(game_logo)
input("Type any key to start the game..")
player_name = input("Type your name: ")
while player_name == "":
    print("Invalid Input!")
    player_name = input("Type your name: ")

print(f"Hey {player_name}, let's start the game!\n")

while game_flag:
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(f"question #{question_n}:")
    key_1 = random.choice(key_list)
    first_quan = quantities_dict[key_1]
    key_2 = random.choice(key_list)
    while key_1 == key_2:
        key_2 = random.choice(key_list)
    second_quan = quantities_dict[key_2]
    print(f"A : {key_1}")
    print(f"B : {key_2}")
    print("\nIs A is Higher or Lower from B ? ")
    ans_player = input("Type 'higher' or 'lower' ---> ").lower()
    while ans_player not in ['higher', 'lower']:
        print("Invalid input!")
        ans_player = input("Type 'higher' or 'lower' ---> ").lower()

    if (first_quan > second_quan and ans_player == "higher") or (second_quan > first_quan and ans_player == "lower"):
        print("")