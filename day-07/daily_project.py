# Hangman Game - Python project (Day 7)

import random

words = ["apple", "mouse", "bedroom", "fire", "lamp", "software", "elephant"]
lives = 6
rand_word = random.choice(words)
art_index = 0

placeholder = []
for i in range(0, len(rand_word)):
    placeholder.append("_")

letter_exist = False
win_flag = False
already_exist = False

display = ""
for i in range(0, len(placeholder)):
    display += placeholder[i]

gui_1 = (
         f"               _______                   \n"
         f"               |      |                  \n"
         f"                      |                  \n"
         f"                     _|_                 \n"
         f"                    [ | ]                \n"
         f" ♥ = 6              ^ ^ ^                \n"
         f"*****************************************")

gui_2 = (
         f"               _______                    \n"
         f"               |      |                   \n"
         f"               O      |                   \n"
         f"                     _|_                  \n"
         f"                    [ | ]                 \n"
         f" ♥ = 5              ^ ^ ^                 \n"
         f"******************************************\n")

gui_3 = (
         f"               _______                    \n"
         f"               |      |                   \n"
         f"               O      |                   \n"
         f"               |     _|_                  \n"
         f"                    [ | ]                 \n"
         f" ♥ = 4              ^ ^ ^                 \n"
         f"******************************************\n")

gui_4 = (
         f"               _______                    \n"
         f"               |      |                   \n"
         f"               O      |                   \n"
         f"             #-|     _|_                  \n"
         f"                    [ | ]                 \n"
         f" ♥ = 3              ^ ^ ^                 \n"
         f"******************************************\n")

gui_5 = (
         f"               _______                    \n"
         f"               |      |                   \n"
         f"               O      |                   \n"
         f"             #-|-#   _|_                  \n"
         f"                    [ | ]                 \n"
         f" ♥ = 2              ^ ^ ^                 \n"
         f"******************************************\n")

gui_6 = (
         f"               _______                    \n"
         f"               |      |                   \n"
         f"               O      |                   \n"
         f"             #-|-#   _|_                  \n"
         f"                L   [ | ]                 \n"
         f" ♥ = 1              ^ ^ ^                 \n"
         f"******************************************\n")

gui_lose = (
            f"               _________                   \n"
            f"               |       |                   \n"
            f"               O       |                   \n"
            f"             #-|-#    _|_                  \n"
            f"              J L    [ | ]                 \n"
            f" ♥ = 0               ^ ^ ^      You Lose !!\n"
            f"******************************************\n")

gui_win = (f"******************************************\n"
           f"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"
           f"    ♥ Y O U                               \n" 
           f"           ♥ A R E                        \n"
           f"                ♥ T H E                   \n"
           f"                      ♥  W I N N E R !!   \n"
           f"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"
           f"******************************************")

gui_art = [gui_1, gui_2, gui_3, gui_4, gui_5, gui_6]


while not win_flag and lives > 0:
    print(f"*******************************************\n"
          f"The word was ---->         {display}       \n")
    print(gui_art[art_index])
    letter = input(f"insert your guess : ").lower()

    if display.__contains__(letter):
        already_exist = True
    else:
        for i in range(0, len(rand_word)):
            if rand_word[i] == letter:
                placeholder[i] = letter
                letter_exist = True

    display = ""
    for i in range(0, len(placeholder)):
        display += placeholder[i]
    if display == rand_word:
        win_flag = True

    print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
    if win_flag:
        print(f"The Word is:    {display}")
        print(gui_win)
    elif already_exist:
        print(f"You already discover that letter - try another!")
        already_exist = False
    elif letter_exist:
        print(f"Good job! this was a great guess!")
        letter_exist = False
    elif not letter_exist and lives == 1:
        print(f"The Word was:    {rand_word}")
        lives -= 1
        print(gui_lose)
    else:
        lives -= 1
        art_index += 1
        print(f"Oops! wrong guess..")



