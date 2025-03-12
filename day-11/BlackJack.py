from art import game_logo,game_rules
import game_functions


game_flag = True

print(game_logo)
input("Press any key to start...")
print("Welcome to my BlackJack Game!")
player_name = input("Please insert your name before we start :\n")

print(f"Hey {player_name} ! are you familiar with BlackJack rules?")
p_ans = input("Type 'y' for yes and 'n' for no ---> ").lower()

while p_ans not in ['y','n']:
    print("Invalid Input!")
    print(f"Hey {player_name} ! are you familiar with BlackJack rules?")
    p_ans = input("Type 'y' for yes and 'n' for no ---> ").lower()

if p_ans == 'n':
    print(game_rules)
    input("Press any key to when you are ready to start...")

player_bank = 1000
computer_bank = 1000
card_pack = game_functions.new_card_pack()

while game_flag:

    round_flag = True
    player_bet = int(input(f"Insert your bet (current - {player_bank} coins in the player's bank) - "))
    computer_bank -= player_bet
    player_bank -= player_bet
    round_price = player_bet*2

    while round_flag:

        player_hand = []
        computer_hand = []
        stand_flag = False

        for i in range(2):
            player_hand.append(game_functions.hit_from_stack(pack=card_pack))
            computer_hand.append(game_functions.hit_from_stack(pack=card_pack))
            if i == 0:
                game_functions.reveal_card(card=player_hand[0])
                game_functions.reveal_card(card=computer_hand[0])

        if game_functions.check_hand_value(hand=computer_hand) < 17:
            game_functions.the_17_rule(c_hand=computer_hand, pack=card_pack)
            if game_functions.check_hand_value(hand=computer_hand) > 21:
                print("Computer's hand value is higher then 21 - Bust!")
                stand_flag = True


        while not stand_flag:
            game_functions.show_hand_cards(hand=player_hand, name=player_name)
            print(f"Your current hand value is {game_functions.check_hand_value( hand=player_hand)} .")
            hit_or_stand = input("to hit a card type 'h' , to stand type 's' ---> ").lower()
            while hit_or_stand not in ['h', 's']:
                print("Invalid Input!")
                print(f"Your current hand value is {game_functions.check_hand_value(hand=player_hand)} .")
                hit_or_stand = input("to hit a card type 'h' , to stand type 's' ---> ").lower()

            if hit_or_stand == 'h':
                print(" <<----------->>  Hit! <<----------->>")
                player_hand.append(game_functions.hit_from_stack(pack=card_pack))
                if game_functions.check_hand_value( hand=player_hand) > 21:
                    print(f"{player_name}'s hand value is higher then 21 - Bust!")
                    stand_flag = True
            else:
                print(" <<----------->>  Stand! <<----------->>")
                stand_flag = True

        print(" <<----------->> BlackJack <<----------->>")
        player_round_hand_value = game_functions.check_hand_value(hand=player_hand)
        computer_round_hand_value = game_functions.check_hand_value(hand=computer_hand)

        game_functions.show_hand_cards(hand=computer_hand)
        print(f"Computer hand value is - {computer_round_hand_value}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        game_functions.show_hand_cards(hand=player_hand, name=player_name)
        print(f"Computer hand value is - {player_round_hand_value}")

        if player_round_hand_value > 21 or player_round_hand_value < computer_round_hand_value <= 21:
            print(f"{player_name} lose !")
            computer_bank += round_price
        elif player_round_hand_value == computer_round_hand_value:
            print("It's a Draw!")
            computer_bank += player_bet
            player_bank += player_bet
        elif computer_round_hand_value < player_round_hand_value <= 21 or computer_round_hand_value > 21




