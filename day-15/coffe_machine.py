from menu_and_resources import MENU, MACHINE_COINS, INGREDIENTS
from art import start_machine,order_in_process
import machine_functions
import time


machine_menu = MENU
machine_ingredients = INGREDIENTS
machine_money_box = MACHINE_COINS


print(start_machine)
time.sleep(3)
machine_functions.clear_screen()
machine_functions.machine_report(machine_ingredients,machine_money_box)