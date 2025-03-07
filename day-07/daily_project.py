# Hangman Game - Python project (Day 7)

import random

words = ["apple", "mouse", "bedroom", "fire", "lamp", "software", "elephant"]
lives = 6
rand_word = random.choice(words)

placeholder = []
for i in range(0, len(rand_word)):
    placeholder.append("_")

letter_exist = False
win_flag = False

display = ""
for i in range(0, len(placeholder)):
    display += placeholder[i]

while not win_flag and lives > 0:
    print(f"----------> {display} <----------")
    letter = input(f"insert your guess").lower()

    for i in range(0, len(rand_word)):
        if rand_word[i] == letter:
            placeholder[i] = letter
            letter_exist = True

    display = ""
    for i in range(0, len(placeholder)):
        display += placeholder[i]
    if display == rand_word:
        win_flag = True

    if win_flag:
        print("The Word is:")
        print(f"----------> {display} <----------")
        print(f"Bravo! you complete the word!")
    elif letter_exist:
        print(f"Success! this was a good guess..")
        letter_exist = False
    else:
        lives -= 1
        print(f"Oops! wrong guess.. youe left with {lives}")



