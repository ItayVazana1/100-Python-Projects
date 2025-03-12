import random

def new_card_pack():

    card_symbols = ['club', 'diamond', 'heart', 'clover']
    card_pack = {}
    for symbol in card_symbols:
        card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        card_pack[symbol] = card_values

    return card_pack


def hit_from_stack(pack):

    card_symbols = ['club', 'diamond', 'heart', 'clover']
    symbol = random.choice(card_symbols)
    card_value = random.choice(pack[symbol])
    if card_value in ['J', 'Q', 'K']:
        card_value = 10
    elif card_value == 'A':
        card_value = int(input("Type the value for this A - 1 or 11 --> "))
        while card_value not in [1,11]:
            print("Invalid Input!")
            card_value = int(input("Type the value for this A - 1 or 11 --> "))
    card = [card_value,symbol]

    return card


def check_hand_value(hand):

    total_hand_value = 0
    for card in hand:
        total_hand_value += card[0]

    return total_hand_value


def the_17_rule(c_hand, pack):

    while sum(c_hand) < 17:
        c_hand.append(hit_from_stack(pack))



def reveal_card(card):
    return f"{card[0]} - {card[1]}"


def show_hand_cards(hand, name="Computer"):
    print(f"{name} hand:")
    for card in hand:
        print(reveal_card(card))
