import os
from art import start_machine,order_in_process
import time

def start_the_machine():
    print(start_machine)
    time.sleep(3)
    clear_screen()


def show_menu(menu):
    print("Welcome to the coffe machine! ☕ ")
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


def clear_screen():
    os.system('cls')
