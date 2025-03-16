import os
from art import start_machine, reboot_machine, turn_off_machine, order_in_process
import time

current_payment_list = []
current_payment_value = 0


def clear_screen():
    os.system('cls')

def start_the_machine():
    print(start_machine)
    time.sleep(3)
    clear_screen()

def reboot():
    print(reboot_machine)
    clear_screen()
    print("Machine is OFF , wait for restart")
    time.sleep(3)
    clear_screen()
    start_the_machine()

def turn_off():
    print(turn_off_machine)
    return False

def show_menu(menu):
    print("\nWelcome to the coffe machine! ☕ ")
    print("what would you like to order?")
    option_counter = 1
    for key in menu:
        print(f"{option_counter}- {key} , {menu[key]['cost']}")
        option_counter += 1
    print("Move to the technical menu by typing 'sys'")

def advanced_mode(advanced_ops):
    print("Choose operation:")
    for key in advanced_ops:
        print(f"{str(key)}:  {advanced_ops[key]}")
    print("Back to the regular menu by typing any other key..")


def machine_report(current_ingredients, current_coins):
    print("***************")
    print("Machine Report")
    print("--------------")
    print("Ingredients:")
    for key in current_ingredients:
        comment = ""
        if current_ingredients[key]['NTR']:
            comment += "(Need Refill)"
        print(f"{key} - {current_ingredients[key]['amount']}{current_ingredients[key]['unit']} {comment}")

    print("\nCoins:")
    total_value = 0
    for key in current_coins:
        print(f"{key} ({current_coins[key]['value']}$) :  {current_coins[key]['count']}")
        total_value += (current_coins[key]['count'] * current_coins[key]['value'])

    print(f"\nTotal value - {round(total_value, 2)}")
    print("--------------")
    print("***************")


def check_resources_amounts(drink, menu, current_ingredients):
    missing_ingredients = []
    ing_list = list(menu[drink]['ingredients'].keys())
    for ingredient in ing_list:
        current_amount = current_ingredients[ingredient]['amount']
        min_amount = current_ingredients[ingredient]['min']
        order_usage = menu[drink]['ingredients'][ingredient]
        if 0 < (current_amount-order_usage) < min_amount:
            current_ingredients[ingredient]['NTR'] = True
        elif current_ingredients[ingredient]['NTR']:
            missing_ingredients.append(ingredient)

    if len(missing_ingredients) != 0:
        print(f"Sorry! Can't supply this type of drink.\nWe are run out of :{missing_ingredients}")
        return False

    return True


def get_purchase(coins):
    global current_payment_list
    global current_payment_value

    total_purchase = 0
    print("Insert the amount of each coin:\n")
    for coin in coins:
        while True:
            try:
                in_coins = int(input(f"{coin}({coins[coin]['value']}$):  "))
            except ValueError:
                print("Invalid Input!")
                in_coins = int(input(f"{coin}({coins[coin]['value']}$):  "))
            finally:
                break

        current_payment_list.append([coin, in_coins])
        total_purchase += in_coins * coins[coin]['value']

    current_payment_value = round(total_purchase, 2)
    return round(total_purchase, 2)



def take_an_order(order, menu, ingredients, coins):

    if order not in menu.keys():
        print("Product is not exist.")
        print("Back to menu..")
        current_payment_list.clear()
        return False
    elif not check_resources_amounts(order, menu, ingredients):
        print("Back to menu..")
        current_payment_list.clear()
        return False
    elif get_purchase(coins) < menu[order]['cost']:
        print("Sorry ... It's not enough money.")
        print("Try to choose another one :)")
        print("Back to menu..")
        current_payment_list.clear()
        return False
    else:
        return True



def calculate_change(order, menu, purchase):

    cost_of_order = menu[order]['cost']

    return purchase - cost_of_order


def take_coins_from_payment(order_cost, coins):

    global current_payment_list

    current_payment_list.reverse()

    value_basket = 0

    for coin_set in current_payment_list:
        coin_value = coins[coin_set[0]]['value']
        for i in range(0, coin_set[1]):
            if coin_value + value_basket < order_cost:
                value_basket += coin_value
                coins[coin_set[0]]['count'] += 1
            elif coin_value + value_basket > order_cost:
                break
            else:
                coins[coin_set[0]]['count'] += 1
                return


def make_order(order, menu, ingredients, coins):

    global current_payment_value

    print(order_in_process)

    order_ingredients = list(menu[order]['ingredients'])

    change = calculate_change(order, menu, current_payment_value)

    order_cost = menu[order]['cost']

    if change != 0:
        take_coins_from_payment(order_cost, coins)

    for oi in order_ingredients:
        ingredients[oi]['amount'] -= menu[order]['ingredients'][oi]


    current_payment_value = 0
    current_payment_list.clear()

    print("Your Order is Ready!")
    if change != 0 :
        print(f"Take your change - {round(change, 2)}$")


