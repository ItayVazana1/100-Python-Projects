# Day 12 - Number Guessing Game!
import random
from art import guess_the_number


# Global Variables and Sentences to re-use
attempts = 10
difficulty = 'easy'
min = 1
max = 100
secret_number = 1
guess_is = ""
game_flag = True
round_flag = True

# Functions to handle the game logic:
def new_num_to_guess():
    global secret_number
    secret_number = random.randint(min,max)


def check_if_correct(guess):
    global guess_is
    global attempts
    global round_flag

    if guess == secret_number:
        guess_is = f"Correct !\nThe number is {secret_number} - well done!"
        round_flag = False
        return
    elif guess < secret_number:
        guess_is = "Too low..\nTry again!"
    else:
        guess_is = "Too high..\nTry again!"

    attempts -= 1
    check_if_lose()


def set_difficulty(diff):

    global difficulty
    difficulty = diff


def set_attempts():
    global difficulty
    global attempts

    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5

def check_if_lose():
    global round_flag

    if attempts == 0:
        print(f"The number was {secret_number}")
        print("You have no more attempts..")
        print("Sorry - you lose!")
        round_flag = False


# The Game itself :
print(guess_the_number)
player_in = input("\nType any key to start..")
while game_flag:
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    print("Choose game difficulty -")
    player_in = input("Type 'easy' or 'hard' --> ")
    while player_in not in ['easy', 'hard']:
        print("Invalid input!")
        print("Choose game difficulty -")
        player_in = input("Type 'easy' or 'hard' --> ")

    set_difficulty(diff=player_in)
    set_attempts()
    new_num_to_guess()
    print("\nI'm thinking of a number between 1 and 100.")

    while round_flag:

        print(f"You have {attempts} attempts remaining to guess the number.\n")

        print("-----------------")
        in_guess = int(input("Make a guess :  "))
        print("-----------------")

        check_if_correct(in_guess)
        print(guess_is)


    player_in = input("If you want to play again type 'a' , otherwise type something else...")
    if player_in == 'a':
        round_flag = True
    else:
        print("Goodbye! :)")
        game_flag = False


