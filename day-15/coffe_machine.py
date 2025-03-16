from menu_and_resources import MENU, MACHINE_COINS, INGREDIENTS, ADVANCED_OPS
import machine_functions



machine_menu = MENU
machine_ingredients = INGREDIENTS
machine_money_box = MACHINE_COINS
machine_advanced_ops = ADVANCED_OPS

machine_functions.start_the_machine()
machine_functions.machine_report(machine_ingredients,machine_money_box)
machine_functions.show_menu(machine_menu)
machine_functions.advanced_mode(ADVANCED_OPS)