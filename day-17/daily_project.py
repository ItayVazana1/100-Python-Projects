# Day 17 - QUIZ game (OOP)
from data_base import statements , art
import random

class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


    def show(self, number):
        print(f"#{number}#  -  {self.text}")
        print("True or False?")


    def check_if_correct(self,bool_ans):
        if bool_ans == self.answer:
            return True
        else:
            return False



def convert_ans_boolean(string_ans):
    if string_ans == "true":
        return True
    else:
        return False


class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.lives = 5


    def update_score(self, is_correct):
        if is_correct:
            print("Correct!")
            self.score += 1
        else:
            print("Wrong! - lose 1 live..")
            self.lives -= 1
            print(f"You have {self.lives} lives remain..")

    def check_if_lose(self):
        if self.lives == 0:
            return True
        else:
            return False


    def game_statics(self):
        print("****************")
        print(f"Player name = {self.name}")
        print(f"Score - {self.score}")
        print("****************")



game_flag = True
question_counter = 1

questions_bank = []

for q_set in statements:
    questions_bank.append(Question(q_set[0],q_set[1]))

print(art)
input("Type any key to start..")

player_name = input("Inser your name:\n")
player = Player(player_name)

print("And the game begin!")
print("----------------------------------------------------")

while game_flag:
    print("\n")
    current_q = random.choice(questions_bank)
    current_q.show(question_counter)
    ans = input("").lower()
    while ans not in ['true','false']:
        print("Invalid input!")
        ans = input("Choose - True or False?\n").lower()
    result = current_q.check_if_correct(convert_ans_boolean(ans))
    player.update_score(result)
    if not player.check_if_lose():
        print("I am sorry..You lose!")
        print("Here is your statistics:")
        game_flag = False
        break
    ask_if_quit = input("\nType 'Q' to Quit now , otherwise type any key when you ready for the next Question..").lower()
    if ask_if_quit == 'q':
        print("It's Ok! - you played well!")
        print("Here is your statistics:")
        Player.game_statics()
        game_flag = False



