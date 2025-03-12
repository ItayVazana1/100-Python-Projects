import time

from art import game_logo,game_rules
import game_functions


game_flag = True

print(game_logo)
input("Press any key to start...")
print("Welcome to my BlackJack Game!")
player_name = input("Please insert your name before we start :\n")
while player_name == "Computer" or player_name == "":
    print("Invalid name!")
    player_name = input("Please insert your name before we start :\n")

print(f"\nHey {player_name} ! are you familiar with BlackJack rules?")
p_ans = input("Type 'y' for yes and 'n' for no ---> ").lower()

while p_ans not in ['y','n']:
    print("Invalid Input!")
    print(f"Hey {player_name} ! are you familiar with BlackJack rules?")
    p_ans = input("Type 'y' for yes and 'n' for no ---> ").lower()

if p_ans == 'n':
    print(game_rules)
    input("Press any key to when you are ready to start...")

print("\nInitialize banks and card pack...")
time.sleep(2)
player_bank = 1000
computer_bank = 1000
card_pack = game_functions.new_card_pack()
print("Shuffle the cards...")
time.sleep(2)

print("\nWe are Ready - Game Start!")
round_counter = 1

while game_flag:

    print("\n-*-*-*-*--*-*-*-*-*-*")
    print(f"       Round {round_counter}")
    print("-*-*-*-*--*-*-*-*-*-*")
    print("Current banks status:")
    print(f"{player_name} bank - {player_bank} coins")
    print(f"Computer bank - {computer_bank} coins\n")

    player_bet = int(input(f"{player_name} - Insert your bet for this round\n(current - {player_bank} coins in the player's bank) - "))
    computer_bank -= player_bet
    player_bank -= player_bet
    round_price = player_bet*2

    player_hand = []
    computer_hand = []
    stand_flag = False

    for i in range(2):
        player_hand.append(game_functions.hit_from_stack(pack=card_pack))
        computer_hand.append(game_functions.hit_from_stack(pack=card_pack))
        if i == 0:
            print("------------------------------")
            print(f"{player_name} first card is   {game_functions.reveal_card(card=player_hand[0])}")
            print(f"Computer first card is   {game_functions.reveal_card(card=computer_hand[0])}")
            print("------------------------------\n")

    while not stand_flag:
        game_functions.show_hand_cards(hand=player_hand, name=player_name)
        print(f"{player_name} - Your current hand value is {game_functions.check_hand_value(hand=player_hand)} .")
        hit_or_stand = input("to hit a card type 'h' , to stand type 's' ---> ").lower()
        while hit_or_stand not in ['h', 's']:
            print("Invalid Input!")
            print(f"{player_name} - Your current hand value is {game_functions.check_hand_value(hand=player_hand)} .")
            hit_or_stand = input("to hit a card type 'h' , to stand type 's' ---> ").lower()

        if hit_or_stand == 'h':
            print("\n <<----------->>  Hit! <<----------->>\n")
            player_hand.append(game_functions.hit_from_stack(pack=card_pack, name=player_name))
            if game_functions.check_hand_value(hand=player_hand) > 21:
                print(f"{player_name}'s hand value is higher then 21 - Bust!")
                stand_flag = True
        else:
            print("\n <<----------->>  Stand! <<----------->>\n")
            stand_flag = True


    if game_functions.check_hand_value(hand=computer_hand) < 17 and game_functions.check_hand_value(hand=player_hand) <= 21:
        game_functions.the_17_rule(c_hand=computer_hand, pack=card_pack)
        if game_functions.check_hand_value(hand=computer_hand) > 21:
            print("Computer's hand value is higher then 21 - Bust!")

    print(f"\n <<----------->> Round #{round_counter} - Summary <<----------->>\n")
    player_round_hand_value = game_functions.check_hand_value(hand=player_hand)
    computer_round_hand_value = game_functions.check_hand_value(hand=computer_hand)

    game_functions.show_hand_cards(hand=computer_hand)
    print(f"Computer hand value is - {computer_round_hand_value}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    game_functions.show_hand_cards(hand=player_hand, name=player_name)
    print(f"{player_name}'s hand value is - {player_round_hand_value}\n")

    if player_round_hand_value > 21 or player_round_hand_value < computer_round_hand_value <= 21:
        print(f"{player_name} lose this round!")
        print("Computer win!")
        computer_bank += round_price
    elif player_round_hand_value == computer_round_hand_value:
        print("It's a Draw!")
        computer_bank += player_bet
        player_bank += player_bet
    elif computer_round_hand_value < player_round_hand_value <= 21 or computer_round_hand_value > 21:
        print(f"{player_name} win this round!")
        print("Computer lose!")
        player_bank += round_price

    continue_or_quit = input("If you want to continue type 'c' , otherwise type something else --> ").lower()
    if continue_or_quit != 'c':
        game_flag = False
    else:
        round_counter += 1


print("\n$$$$$$$$$$$$$ Game Over $$$$$$$$$$$$$\n")
print(f"Rounds = {round_counter}\n\nResults:")
print(f"Computer Bank - {computer_bank} coins")
print(f"{player_name} Bank - {player_bank} coins\n")
print("\nThe Winner is..\n")
if player_bank > computer_bank:
    print(f"{player_name}! Well done!")
elif player_bank == computer_bank:
    print(f"No one - It's a Draw!")
else:
    print("The Computer!")

print("status of the pack")
for key in card_pack:
    print(card_pack[key])


