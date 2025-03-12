import random
from art import symbols_signs

def new_card_pack():

    card_symbols = ['club', 'diamond', 'heart', 'spade']
    card_pack = {}
    for symbol in card_symbols:
        card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        card_pack[symbol] = card_values

    return card_pack


def hit_from_stack(pack, name="Computer"):

    card_symbols = ['club', 'diamond', 'heart', 'spade']
    symbol = random.choice(card_symbols)
    while len(pack[symbol]) == 0:
        card_symbols.remove(symbol)
        symbol = random.choice(card_symbols)
        if len(card_symbols) == 0:
            pack = new_card_pack()

    card_value = random.choice(pack[symbol])
    pack[symbol].remove(card_value)

    c_suit = {
        'club': 0 ,
        'diamond': 1 ,
        'heart': 2,
        'spade': 3
    }

    if card_value in ['J', 'Q', 'K']:
        card_value = 10
    elif card_value == 'A':
        if name == "Computer":
            card_value = 1
        else:
            card_value = int(input("Type the value for this A - 1 or 11 --> "))
            while card_value not in [1,11]:
                print("Invalid Input!")
                card_value = int(input("Type the value for this A - 1 or 11 --> "))

    card = [card_value, symbol, symbols_signs[c_suit[symbol]]]

    return card


def check_hand_value(hand):

    total_hand_value = 0
    for card in hand:
        total_hand_value += card[0]

    return total_hand_value


def the_17_rule(c_hand, pack):

    while check_hand_value(c_hand) < 17:
        c_hand.append(hit_from_stack(pack))


def reveal_card(card):
    return f"{card[0]} - {card[2]} {card[1]}"


def show_hand_cards(hand, name="Computer"):
    print(f"{name} hand:")
    for card in hand:
        print(reveal_card(card))
