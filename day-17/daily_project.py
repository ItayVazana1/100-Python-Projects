# Day 17 - QUIZ game (OOP)
from data_base import statements , art
import random

class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


        def show(number):
            print(f"#{number}#  -  {text}")
            print("True or False?")


class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.lives = 5

        def get_name():
            return name

        def update_score(is_correct):
            if is_correct:
                self.score += 1
            else:
                self.lives -= 1

        def check_if_lose():
            if self.lives == 0:
                return True
            else:
                return False


        def game_statics():
            print("****************")
            print(f"Player name = {self.name}")
            print(f"Score - {self.score}")
            print("****************")



game_flag = True

print()
while game_flag