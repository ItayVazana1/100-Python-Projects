import os
from art import start_machine, reboot_machine, turn_off_machine, order_in_process
import time

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

def turn_off(flag):
    print(turn_off_machine)
    flag = False

def show_menu(menu):
    print("\nWelcome to the coffe machine! ☕ ")
    print("what would you like to order?")
    option_counter = 1
    for key in menu:
        print(f"{option_counter}- {key} , {menu[key]['cost']}")
        option_counter += 1


def advanced_mode(advanced_ops):
    print("Choose operation:")
    for key in advanced_ops:
        print(f"{str(key)}:  {advanced_ops[key]}")


def machine_report(current_ingredients, current_coins):
    print("***************")
    print("Machine Report")
    print("--------------")
    print("Ingredients:")
    for key in current_ingredients:
        print(f"{key} - {current_ingredients[key]['amount']}{current_ingredients[key]['unit']}")

    print("\nCoins:")
    total_value = 0
    for key in current_coins:
        print(f"{key} ({current_coins[key]['value']}$) :  {current_coins[key]['count']}")
        total_value += (current_coins[key]['count'] * current_coins[key]['value'])

    print(f"\nTotal value - {total_value}")
    print("--------------")
    print("***************")


def check_resources_amounts(drink, menu, current_ingredients):
    missing_ingredients = []
    ing_list = list(menu[drink]['ingredients'].keys())
    for ingredient in ing_list:
        current_amount = current_ingredients[ingredient]['amount']
        min_amount = current_ingredients[ingredient]['min']
        order_usage = menu[drink]['ingredients'][ingredient]
        if (current_amount-order_usage) < min_amount:
            missing_ingredients.append(ingredient)

    if len(missing_ingredients) != 0:
        print(f"Sorry! Can't supply this type of drink.\nWe are run out of :{missing_ingredients}")
        return False

    return True


def get_purchase(coins):

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

        total_purchase += in_coins * coins[coin]['value']

    return round(total_purchase,2)



def take_an_order(order, menu, ingredients, coins):

    if order not in menu.keys():
        print("Product is not exist in the menu.")
    elif not check_resources_amounts(order, menu, ingredients):
        return
    elif get_purchase(coins) < menu[order]['cost']:
        print("Sorry ... It's not enough money.")
    else:
        make_order()


def make_order():
    print("working on it..")