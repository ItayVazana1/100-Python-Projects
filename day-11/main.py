# Day 11 - 100 Days of Code - Python

# Project to summarize the progress until now.
# It will cover all topics which learned so far.
# The project is BlackJack Capstone game

# Game rules:
# one-player game (in this version)
# the player have a bank (his coins)
# each round the player put a gamble (amount from his bank).
# when a round is finished - there is no reuse of cards!
# when all cards are out from game - a new pack is out.
# the game ends when :
# option 1 - the player choose to quit (after each round he can do it)
# then his bank amount compared to this of the computer (start with same amount).
# the winner is the side with higher bank.
# option 2 - player run out of chips - the player lose

# how a round is going :
# both player and computer starts with 1 "shown" card (public)
# after that - both player and computer get 1 more "hidden" card (private)
# at this part - each side have one exposed card and one hidden card.
# the purpose of the player - raise the sum of the cards on the
# table with the card in his hand - but make sure
# that the sum stay under or equal 21.
# the hand with the highest value - wins.
# before check the cards - its possible to get more card from stack.
# it can make the player closer to 21 , but can also make him lose:
# if the sum is more than 21 - it's called bust ,
# and this is immediate win to the computer.

# specific rule :
# the "17 rule" - in each computer's turn - if the
# sum of his cards lower than 17 - * he must * to take one card from stack.
# it's need to continue until the sum of computer hand is 17 or higher.


# the value of the cards -
# from 2 to 10 = the same as the number.
# J , Q , K = 10
# Ace - can be 1 or 11 (based on the player choice).

# possible result for game:
# 1 - player hand is greater from computer hand but equal or less 21 - player win
# 2 - player hand is lower from computer hand - and the computer hand is equal or less 21 - computer win
# 3 - both player and computer hands equals but equal or less 21 - draw
# 4 - player hand is greater from computer hand , and it values more than 21 - computer win
# 4 - computer hand is greater from computer hand , and it values more than 21 - player win



